cmake_minimum_required(VERSION 3.20)
project(main VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)

include(lib_paths.cmake)

# MPFR & GMP
include_directories(${MPFR_INCLUDE_PATH})
include_directories(${GMP_INCLUDE_PATH})

find_library(MPFR_LIB mpfr PATHS ${MPFR_INCLUDE_PATH})
find_library(GMP_LIB gmp PATHS ${GMP_INCLUDE_PATH})

add_library(main SHARED main.cpp
    brutus_code/Star.cpp
    brutus_code/Cluster.cpp
    brutus_code/Brutus.cpp
    brutus_code/Bulirsch_Stoer.cpp
)


# Link MPFR
target_link_libraries(main PRIVATE ${MPFR_LIB})
target_link_libraries(main PRIVATE ${GMP_LIB})


# Install
install(TARGETS main DESTINATION ${CMAKE_CURRENT_LIST_DIR}/brutus/lib)

install(FILES main.py DESTINATION ${CMAKE_CURRENT_BINARY_DIR})