import pandas as pd
import ctypes

from ..common import Cluster


class BaseOutput:
    """Base class for output handlers.

    Output handlers are responsible for processing the simulation's output format and generating a useful result.

    If you want to create a new output handler, you should start by subclassing this class and implementing the
    receive_output_line, finalize, and result methods.
    """
    def receive_output_line(self, line: str):
        """Method that processes a single line of output from the simulation.

        The simulation will output its state at each time step, which is passed to this method as a string.
        This method should parse the string and store the relevant information in the intended data structure.
        """
        raise NotImplementedError()

    def finalize(self):
        """Method that finalizes the output processing.

        This method is called after all output lines have been processed.
        It should be used to finalize the output processing and prepare the result for retrieval.
        """
        raise NotImplementedError()

    def result(self):
        """Method that returns the final result of the output processing.

        This method should return the final result of the output processing, which can be any data structure.
        """
        raise NotImplementedError()


class RawOutput(BaseOutput):
    """Output handler that stores the raw output from the simulation.

    This output handler simply stores the raw output from the simulation as a list of strings.
    """
    def __init__(self):
        super().__init__()
        self.data = []

    def receive_output_line(self, line: str):
        self.data.append(line)

    def finalize(self):
        pass  # No finalization needed for raw output

    def result(self):
        return self.data


class PandasOutput(BaseOutput):
    """Output handler that generates a pandas DataFrame from the simulation output.

    The output columns will be as follows:
    - time: The time at which the state was recorded
    - star_count: The number of stars in the cluster
    - star_<identifier>_pos: The position of star <identifier> as a list [x, y, z]
    - star_<identifier>_vel: The velocity of star <identifier> as a list [vx, vy, vz]
    - star_<identifier>_mass: The mass of star <identifier>
    - total_energy: The total energy of the system
    - kinetic_energy: The kinetic energy of the system
    - potential_energy: The potential energy of the system
    """
    def __init__(self, cluster: Cluster, sep: str = ','):
        super().__init__()

        self.cluster = cluster
        self.sep = sep

        self.data = []  # Stores the output data as a list of dictionaries, which will be converted to a DataFrame on finalize
        self.df: pd.DataFrame | None = None  # Stores the final DataFrame

    def receive_output_line(self, line: str):
        values = line.strip().split(self.sep)
        row = PandasOutput._parse_output_line(values)
        self.data.append(row)

    def finalize(self):
        self.df = pd.DataFrame(self.data)

    def result(self):
        if self.df is None:
            raise ValueError('No output data available. Make sure to call finalize before retrieving the results.')
        return self.df

    @staticmethod
    def _parse_output_line(values):
        t, star_count = values[0], values[1]
        t, star_count = float(t), int(star_count)

        stars = []
        for i in range(star_count):
            star = {
                'identifier': int(values[2 + i * 8]),
                'position': [float(values[3 + i * 8]), float(values[4 + i * 8]), float(values[5 + i * 8])],
                'velocity': [float(values[6 + i * 8]), float(values[7 + i * 8]), float(values[8 + i * 8])],
                'mass': float(values[9 + i * 8]),
            }
            stars.append(star)

        total_energy = float(values[-3])
        kinetic_energy = float(values[-2])
        potential_energy = float(values[-1])

        row = {
            'time': t,
            'star_count': star_count,
            'total_energy': total_energy,
            'kinetic_energy': kinetic_energy,
            'potential_energy': potential_energy,
        }

        for star in stars:
            row.update({
                f'star_{star["identifier"]}_pos': star['position'],
                f'star_{star["identifier"]}_vel': star['velocity'],
                f'star_{star["identifier"]}_mass': star['mass']
            })

        return row
