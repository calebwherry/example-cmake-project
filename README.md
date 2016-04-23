# example-cmake-project

Example CMake Structure for C++ Projects with Python Build Wrapper

[![Build Status](https://travis-ci.org/calebwherry/example-cmake-project.svg?branch=master)](https://travis-ci.org/calebwherry/example-cmake-project)

## Requirements

* CMake 3
* Python 2/3
* C++11 compliant compiler such as:
 + GCC 4.8
 + Clang 3.5
 + MSVC 18.0
 + Intel 14.0
* Boost 1.50.0

To support a new compiler, edit the `cmake_modules/CompilerOptions.cmake` and add the new compiler ID along with the needed compiler flags.
