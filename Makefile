
compile:
	mkdir -p build && cd build && cmake ..
	cd build && cmake --build . -j 4

install:
	cd build && make install

run:
	cd build && python3 main.py

clean:
	rm -rf build
	find ./brutus -name "__pycache__" -exec rm -rf {} \;
