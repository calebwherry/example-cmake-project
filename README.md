# example-cmake-project

Example CMake Structure for C++ Projects with Python Build Wrapper

Linux + Mac: [![Build Status](https://travis-ci.org/calebwherry/example-cmake-project.svg?branch=master)](https://travis-ci.org/calebwherry/example-cmake-project)
Windows: [![Build status](https://ci.appveyor.com/api/projects/status/41xl917ixa8olab4?svg=true)](https://ci.appveyor.com/project/calebwherry/example-cmake-project)

## Requirements (oldest versions tested are given)

* CMake 3
* Python 2/3
* C++11 compliant compiler such as:
 + GCC 4.9
 + Clang 3.7
 + MSVC 19.0 (Visual Studio 2015)
 + Intel 15.0

To support a new compiler, edit the `cmake_modules/CompilerOptions.cmake` and add the new compiler ID along with the needed compiler flags.
