Extending Output Handlers
=========================

If you need the simulation results to output to a specific format, you can easily create your own OutputHandlers by subclassing the :class:`brutus.BaseOutput`.

This section will help you understand this class and how to create your own output format.

Base Class Structure
--------------------

The :class:`brutus.BaseOutput` class includes four methods:

.. py:method:: BaseOutput.__init__(self, cluster: brutus.Cluster)

    The constructor for the BaseOutput class. This method should be called by the subclass constructor. The BaseOutput automatically creates the cluster class attribute, which can be accessed by the subclass using ``self.cluster``.

    :param cluster: The cluster object that the BaseOutput will be attached to.
    :type cluster: :class:`brutus.Cluster`

.. py:method:: BaseOutput.receive_output_line(self, line: str)

    This method is called by the simulation when a new line of output is ready to be processed. A new line of output is available every time the simulation eveolves to a new time step.

    :param line: The new line of output.
    :type line: str

.. py:method:: BaseOutput.finalize(self)

    This method is called by the simulation when the simulation is complete. This method should be used to finalize the output and write it to the desired location or create the final output object ready for retrieval.

.. py:method:: BaseOutput.result(self)

    This method should return the final output object. Called when the simulation as a whole is complete.

Output Line Format
------------------

The output line format is a comma-separated string that represents the output of the simulation at a specific time step. The output line format is determined by the simulation and is passed to the BaseOutput using the :meth:`BaseOutput.receive_output_line` method.

Its format is as follows:

1. The current time step
2. The number of stars
3. For each star in the cluster

 a. The star's identifier
 b. The star's x-coordinate
 c. The star's y-coordinate
 d. The star's z-coordinate
 e. The star's x-velocity
 f. The star's y-velocity
 g. The star's z-velocity
 h. The star's mass

4. The total energy of the cluster
5. The total kinetic energy of the cluster
6. The total potential energy of the cluster

Values should be interpreted as floats except for the number of stars and the star's identifier, which should be interpreted as integers.

Creating a New Output Handler
-----------------------------

As mentioned earlier, to create a new output handler, you need to subclass the :class:`brutus.BaseOutput` class. Here is an example of a simple output handler that writes the output to a file:

.. code-block:: python

    from brutus import BaseOutput

    class FileOutputHandler(BaseOutput):
        def __init__(self, cluster):
            super().__init__(cluster)
            self.file = open(f'{cluster.name}.txt', 'w')

        def receive_output_line(self, line: str):
            self.file.write(line)

        def finalize(self):
            self.file.close()

        # Ignore the result method
        def result(self):
            pass

This output handler will write the output to a file with the same name as the cluster. To use this output handler, you can pass it to the cluster when creating it:

.. code-block:: python

    from brutus import BrutusIntegrator, Cluster

    cluster = Cluster(...)

    integrator = BrutusIntegrator(...)
    integrator.add_cluster(cluster, output_handler=FileOutputHandler(cluster))
