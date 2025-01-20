Installation
============

.. important:: Please read these instruction carefully before proceeding with the installation. The installation process is a little bit more complicated than standard Python packages due to the existence of a C++ backend. This walkthrough will guide you through the entire process.

Dependencies - Overview
-----------------------

.. caution:: This package is only available for MacOS and Linux. Windows is not supported.

Before installing the Brutus Python interface, you will need a few dependencies, which, depending on your system,
can be more or less complicated to install:

#. **C++ compiler**: The main compiler
#. **CMake**: A build management tool used to build the C++ backend
#. **Make**: A build automation tool used to build the whole projec, including these docs
#. **MPFR and GMP**: The GNU Multiple Precision Arithmetic Library and the GNU Multiple Precision Library, respectively. These libraries are used to perform high-precision arithmetic operations in Brutus.
#. **Python 3.6 or later**: The Python interpreter to run the Brutus Python interface
#. **PIP (optional)**: The Python package manager, used to install the Brutus Python interface into your Python environment
#. **A Python virtual environment (optional, but recommended)**: To contain the dependencies of the Brutus Python interface and avoid conflicts with other Python packages

.. note :: **If on MacOS**, install `Homebrew <https://brew.sh/>`_ to simplify the installation of the dependencies. The commands below will assume that you have Homebrew installed.

Step 0 - Clone the repository
-----------------------------

The first step is to clone the repository to your local machine. This can be done using GIT or by downloading the repository as a ZIP file from the GitHub page.

Step 1 - Install the dependencies
---------------------------------

The first step is to install the dependencies. The exact process will depend on your operating system/package manager, but here are some general guidelines:

**For MacOS using Homebrew**:

.. code-block:: bash

    # Download the C++ compiler, make, and CMake (grab some coffee/tea, this will take a while)
    sudo xcode-select --install

    # Download the MPFR and GMP libraries
    brew install mpfr gmp

    # Download Python 3.6 or later (if not already installed)
    # This will also install PIP
    brew install python3

**For Ubuntu/Debian**:

.. code-block:: bash

    # Download the C++ compiler, make, and CMake
    sudo apt-get install build-essential cmake

    # Download the MPFR and GMP libraries
    sudo apt-get install libmpfr-dev libgmp-dev

    # Download Python 3.6 or later with PIP
    sudo apt-get install python3 python3-pip

Step 2 - Update the CMake configuration
---------------------------------------

The next step is to update the CMake configuration to point to the MPFR and GMP libraries, which will have to be built with and linked to the project. Firstly, you have to find the paths to the MPFR and GMP libraries, which can be done with the following commands:

**For MacOS using Homebrew**:

.. code-block:: bash

    # Returns the path to the MPFR library
    brew --prefix mpfr

    # Returns the path to the GMP library
    brew --prefix gmp  

**For Ubuntu/Debian**:

.. code-block:: bash

    # Returns the path to the MPFR library
    ldconfig -p | grep mpfr

    # Returns the path to the GMP library
    ldconfig -p | grep gmp

Secondly, the `lib_paths.cmake` file in the project's root folder has to be updated with the paths to the MPFR and GMP libraries. However, **append the "include" suffix to the returned paths**. For example, the path `/opt/homebrew/Cellar/mpfr` should be updated to `/opt/homebrew/Cellar/mpfr/include` before
being added to the `lib_paths.cmake` file.

The resulting file should look like this (please update the paths according to your system):

.. code-block:: cmake

    set(MPFR_INCLUDE_DIR "/opt/homebrew/Cellar/mpfr/include")
    set(GMP_INCLUDE_DIR "/opt/homebrew/Cellar/gmp/include")

.. note:: For those who are familiar with C++'s include and link phases, only the include path is necessary. The lib path should be automatically discovered by CMake.

Step 3 - Build the project
--------------------------

After having updated the `lib_paths.cmake` file, you can now build the project. This is done by running the following commands in the project's root folder:

.. code-block:: bash

    make  # Builds the project
    make install  # Moves the resulting shared library to the Python package folder

Step 4 - Install the Python interface
-------------------------------------

Finally, you're ready to install the Python interface. This is done using your favourite Python package manager, which can be either PIP or Conda. In this example, we will use PIP:

.. code-block:: bash

    pip install .

And that's it! You should now have the Brutus Python interface installed in your Python environment. To test if everything is working correctly, you can run the following command:

.. code-block:: bash

    python -c "import brutus"

If no errors are raised, then everything is working correctly.

(Optional) Cleaning up
----------------------

If you want to clean up the project build files and return the building state to its initial state, you can run the following command:

.. code-block:: bash

    make clean

This will remove all build files, docs, and the installed shared library from the Python package folder.

.. caution:: This will not remove the Python package from your Python environment. To do that, you will have to run `pip uninstall brutus`.


(Optional) Building the documentation
---------------------------------------------

If you want to build the documentation, you can do so by running the following command:

.. code-block:: bash

    make docs

This will create a folder called `docs_html` in the project's root folder, which contains the documentation in HTML format. Open the `index.html` file in your browser to view the documentation.


(Optional) Running the tests
----------------------------

.. note:: To run the tests, you will need to have run the intallation steps at least until the `make install` command.

If you want to run the tests, you can do so by running the following command after having installed the Python environment requirements:

.. code-block:: bash

    pytest
