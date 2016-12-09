# example-cmake-project

Learning and setting up a C++ project that builds CMake can be a daunting task sometimes, especially if you have a complicated build structure. This is an example project that hopefully gives you a starting point to do a lot of awesome things in a CMake project from day 1. It has support of Windows, Linux, and Mac and has automated build tests for all 3 with multiple compilers. Adding new compilers and systems should be easy since you can just follow the structure I have laid out.

Linux + Mac (Travis CI): [![Build Status](https://travis-ci.org/calebwherry/example-cmake-project.svg?branch=master)](https://travis-ci.org/calebwherry/example-cmake-project)

Windows (AppVeyor): [![Build status](https://ci.appveyor.com/api/projects/status/41xl917ixa8olab4?svg=true)](https://ci.appveyor.com/project/calebwherry/example-cmake-project)

## Requirements (oldest versions tested are given)

* CMake 3
* Python 2/3 (only needed if using Python build script)
* C++11 compliant compiler such as:
 + GCC 5.0
 + Clang 3.7
 + MSVC 19.0 (Visual Studio 2015)
 + Intel 15.0

To support a new compiler, edit the `cmake_modules/CompilerOptions.cmake` and add the new compiler ID along with the needed compiler flags.
