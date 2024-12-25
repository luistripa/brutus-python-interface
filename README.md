
# Brutus Python interface

This project is a Python interface for the Brutus integrator. It is a wrapper around the Brutus C++ code.

# Table of contents
- [Brutus Python interface](#brutus-python-interface)
- [Table of contents](#table-of-contents)
- [Example](#example)
- [Installation](#installation)
  - [Pre-requisites](#pre-requisites)
  - [Steps](#steps)

# Example

The following example shows a simple simulation of a 3-body system.

```python
import brutus as br

# Create a Brutus object
cluster = br.Cluster(
    stars=[
        br.Star(identifier=0, position=[0, 0, 0], velocity=[0, 0, 0], mass=1),
        br.Star(identifier=1, position=[1, 0, 0], velocity=[0, 1, 0], mass=1),
        br.Star(identifier=2, position=[0, 1, 0], velocity=[0, 0, 1], mass=1),
    ],
)

# Create a Brutus simulation
brutus = br.BrutusIntegrator(time_step=0.1)
brutus.add_cluster(cluster, output_handler=br.PandasOutput(cluster))

results = brutus.evolve(1)

print(results[0])
```


# Installation

Installing the package is a bit more complicated than usual packages, given that it depends on C++ code that needs to be compiled. The following steps show how to compile the code.

## Pre-requisites

1. MPFR library
2. GMP library
3. CMake
4. A C++ compiler
5. Make
6. Git (optional but recommended)
7. Python 3.6 or later
8. Pip
9. A virtual environment (optional but recommended)

## Steps

1. Install the MPFR and GMP libraries

```bash
# Linux (Ubuntu)
sudo apt-get install libmpfr-dev libgmp-dev

# MacOS
brew install mpfr gmp
```

2. Find the path to the MPFR and GMP libraries

```bash
# Linux
ldconfig -p | grep mpfr
ldconfig -p | grep gmp

# MacOS
brew --prefix mpfr
brew --prefix gmp
```

3. Clone the repository using Git or download the code as a zip file

4. Create a virtual environment (optional but recommended)

5. Update the `lib_paths.cmake` file with the paths to the MPFR and GMP libraries' `include/` directories. The file should look like this:

```cmake
set(MPFR_INCLUDE_PATH "/path/to/mpfr/include")
set(GMP_INCLUDE_PATH "/path/to/gmp/include")
```

6. Compile the code

```bash
make  # This will compile the code into a shared library

make install  # This copies the shared library into the `brutus` package directory
```

7. Install the Python package

```bash
pip install .
```

8. Test the installation

```bash
python3 -c "import brutus"
```
