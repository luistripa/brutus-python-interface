Usage
=====

Using the Brutus Python interface is very simple. This interface has three main objects:

#. The :class:`brutus.Star` class, which represents a star, with position, velocity, and mass.
#. The :class:`brutus.Cluster` class, which represents a system of stars. It's essentially a collection of stars.
#. The :class:`brutus.BrutusIntegrator` class, which contains logic for integrating the system of stars.

Defining a star
---------------

To define a star, you can use the :class:`brutus.Star` class. Here's an example:

.. code-block:: python

    from brutus import Star

    star = Star(identifier=0, position=(0, 0, 0), velocity=(0, 0, 0), mass=1)

This creates a star with identifier 0, at the coordinates (0, 0, 0), with no velocity, and a mass of 1.
Positions and velocities are represented as 3-tuples of floats, and mass is a float.

The star identifier is used for output purposes and must be different for each star in a cluster.
Different clusters can have the same star identifiers.

If one of the parameters has an incorrect size, a :class:`ValueError` will be raised:

.. code-block:: python

    from brutus import Star

    # This will raise a ValueError (position and velocity must be 3-tuples)
    star = Star(identifier=0, position=(0, 0), velocity=(0, 0), mass=1)

Defining a cluster
------------------

To define a cluster, you can use the :class:`brutus.Cluster` class. Here's an example:

.. code-block:: python

    from brutus import Cluster

    cluster = Cluster(
        name='example_cluster',
        stars=[
            Star(identifier=0, position=(0, 0, 0), velocity=(0, 0, 0), mass=1),
            Star(identifier=1, position=(1, 0, 0), velocity=(0, 0, 0), mass=1),
        ]
    )

A cluster represents a system of stars, which will be simulated together.
A cluster can contain any number of stars.
The cluster name is used exclusively for logging purposes and should be unique for each cluster (even though no error will be raised if it isn't).

Integrating the system
----------------------

To integrate the system of stars, you should use the :class:`brutus.BrutusIntegrator` class.
You will also have to define in which format you want the output to be. This can be done by defining an output handler, which currently has two options: `RawOutput` or `PandasOutput`.

.. note:: You can also define your own output handler by subclassing the :class:`brutus.OutputHandler` class.

.. code-block:: python

    from brutus import Cluster, BrutusIntegrator, PandasOutput
    
    cluster = Cluster(...)

    integrator = BrutusIntegrator(time_step=0.1)
    brutus.add_cluster(cluster, output_handler=PandasOutput(cluster))

    results = integrator.evolve(1)  # Simulate for 1 time unit

The results will be stored in the `results` variable, which is a list of the output handler's output format. In this case, it will be a list with a single pandas DataFrame.

Multiple clusters
-----------------

You can also simulate multiple clusters in parallel. To do this, simply define the number of workers you want to use in the :class:`BrutusIntegrator` constructor:

.. code-block:: python

    from brutus import Cluster, BrutusIntegrator, PandasOutput
    
    cluster1 = Cluster(...)
    cluster2 = Cluster(...)

    integrator = BrutusIntegrator(time_step=0.1, workers=2)
    brutus.add_cluster(cluster1, output_handler=PandasOutput(cluster1))
    brutus.add_cluster(cluster2, output_handler=PandasOutput(cluster2))

    results = integrator.evolve(1)  # Simulate for 1 time unit

The results will be a list containing two pandas DataFrames, each with the results of the simulation for each cluster.

.. note:: The number of workers should not exceed the number of clusters you are simulating nor the number of CPU cores/threads in your machine.

.. note:: The parallel computing functionality is implemented using the :mod:`multiprocessing` module, but the N-Body integration is done using the C++ library compiled in the :doc:`installation` step.

Other examples
--------------

For more examples, check the `examples` directory in the repository. There, you will find examples of how to use the Brutus Python interface to simulate different systems of stars.