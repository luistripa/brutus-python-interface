
.PHONY: docs

compile: cmake  # Creates the build directory and compiles the project
	cmake --build build -j 2

cmake:  # Creates the build directory
	mkdir -p build
	cmake -S . -B build

install:  # Installs the Brutus shared library into the python package, making it ready to be installed in the system
	cmake --install build

clean:  # Cleans the build files and the documentation
	rm -rf build
	rm -rf build_docs
	rm -rf docs_html
	rm -rf **/*.dylib
	rm -rf **/*.so
	find ./brutus -name "__pycache__" -exec rm -rf {} \; 2> /dev/null

docs:  # Generates the documentation
	python -m sphinx -T -b html -d build_docs/doctrees -D language=en ./docs/source docs_html