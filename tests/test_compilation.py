import os.path


def test_library_exists():
    assert os.path.exists( os.path.join('brutus', 'lib', 'libmain.dylib') ) or \
              os.path.exists( os.path.join('brutus', 'lib', 'libmain.so') )
