import ctypes


class BrutusInterface:
    """A Python interface to the Brutus integrator library. The interface
    provides methods to initialize a cluster, add stars to it, evolve the
    cluster, and clean up resources. The interface is implemented using
    ctypes to call functions in the Brutus library."""

    def __init__(self):
        self.lib = ctypes.CDLL('./libmain.dylib')

        self.seed_t = ctypes.c_char_p
        self.time_t = ctypes.c_double
        self.star_identifier_t = ctypes.c_int
        self.mass_t = ctypes.c_double
        self.position_t = ctypes.c_double * 3
        self.velocity_t = ctypes.c_double * 3

        self.lib.initCluster.argtypes = [self.seed_t]
        self.lib.addStar.argtypes = [self.star_identifier_t, self.mass_t, self.position_t, self.velocity_t]
        self.lib.evolve.argtypes = [self.time_t, self.time_t, ctypes.CFUNCTYPE(None, ctypes.c_char_p)]
        self.lib.cleanup.argtypes = None

        self.lib.initCluster.restype = None
        self.lib.addStar.restype = None
        self.lib.evolve.restype = None
        self.lib.cleanup.restype = None

    def init_cluster(self, seed: str):
        """Initialize a cluster with the given seed."""
        self.lib.initCluster(seed.encode("utf-8"))

    def add_star(self, identifier: int, mass: float, position: tuple, velocity: tuple, callback):
        """Add a star to the cluster with the given mass, position, and velocity."""
        self.lib.addStar(identifier,
                         mass,
                         self.position_t(*position),
                         self.velocity_t(*velocity),
                         callback)
        
    def evolve(self, time: float, step_time: float, callback):
        """Evolve the cluster for the given time."""
        self.lib.evolve(time, step_time, callback)

    def cleanup(self):
        self.lib.cleanup()


@ctypes.CFUNCTYPE(None, ctypes.c_char_p)
def result_callback(result: str):
    print(result)

interface = BrutusInterface()
interface.init_cluster("id1")
interface.add_star(0, 1.0, (1.0, 2.0, 3.0), (1, 1, 1))
interface.evolve(1.0, 0.5, result_callback)
interface.cleanup()

print("Done")
