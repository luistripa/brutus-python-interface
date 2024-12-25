from dataclasses import dataclass, field


@dataclass(frozen=True)
class Star:
    """A class to represent a star.

    Holds information about the star's position, velocity, and mass.
    """
    identifier: int
    position: list[float]
    velocity: list[float]
    mass: float

    def __post_init__(self):
        """Validate the input parameters."""
        if len(self.position) != 3:
            raise ValueError("Position must be a 3D vector.")
        if len(self.velocity) != 3:
            raise ValueError("Velocity must be a 3D vector.")
        if self.mass <= 0:
            raise ValueError("Mass must be positive.")


@dataclass(frozen=True)
class Cluster:
    """A class to represent a star cluster.

    Holds information about the stars in the cluster and the parameters to be used in the simulation.
    """
    stars: list[Star] = field(default_factory=list)