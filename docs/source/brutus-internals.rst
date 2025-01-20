What is Brutus?
===============

Brutus is a high-precision n-body integrator capable of simulating the
dynamics of a large number of point-mass particles (also called stars, in this context). This integrator is
used extensively in the field of orbital dynamics to simulate the
evolution of planetary systems, star clusters, and other gravitationally
bound systems.

Brutus is written in C++, making it fast and efficient. However, due to the
C++'s inherent complexity, it can be difficult to use for those who are not
familiar with the language. To make Brutus more accessible to a wider audience,
this Python interface was developed.

.. note:: This Python interface and its authors are in no way affiliated with the original authors of the Brutus integrator.


Brutus Internal Workings - High Level Overview
----------------------------------------------

The C++-based Brutus has three main components:

#. **The Brutus main class**, which contains the main simulation loop and the functions to initialize and run it;
#. **The Star class**, which contains information about each star in the simulation;
#. **The Cluster class**, which contains information about a star cluster, such as the number of stars, the initial conditions, and functions to update the positions and velocities of the stars;

.. note:: The Python interface is built on top of these classes, meaning similar names are used.

After setting up the initial conditions of the simulation, the Brutus integrator then uses
the Bulirsch-Stoer method to integrate the star's motion equations. This method is a
high-precision integrator that is well-suited for simulating the long-term evolution of
gravitationally bound systems.