########################################
## \file   CMakeLists.txt
## \date   01/01/2014
## \brief  Main project CMake file.
########################################


#
# Minimum CMake version:
#
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)


#
# Project Properties:
#
project(ExampleCMakeProject CXX)
set(${PROJECT_NAME}_MAJOR_VERSION 1)
set(${PROJECT_NAME}_MINOR_VERSION 0)
set(${PROJECT_NAME}_PATCH_VERSION 0)
set(${PROJECT_NAME}_VERSION 
  ${${PROJECT_NAME}_MAJOR_VERSION}.${${PROJECT_NAME}_MINOR_VERSION}.${${PROJECT_NAME}_PATCH_VERSION}
)


#
# Override some variables if not set: 
#

# Build type:
if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Debug" CACHE STRING "Build type." FORCE)
else()
  set(CMAKE_BUILD_TYPE ${buildType} CACHE STRING "Build type." FORCE)
endif()

# Shared libs:
if (NOT DEFINED BUILD_SHARED_LIBS)
  set(BUILD_SHARED_LIBS ON CACHE STRING "Build libraries as shared." FORCE)
endif()

# Boost:
if ("${BUILD_SHARED_LIBS}" STREQUAL "OFF")
  set(Boost_USE_STATIC_LIBS ON)
else()
  set(Boost_USE_STATIC_LIBS OFF)
endif()


#
# Print useful CMake info:
#
message(STATUS "Project           : ${PROJECT_NAME}")
message(STATUS "Project version   : ${${PROJECT_NAME}_VERSION}")
message(STATUS "Build type        : ${CMAKE_BUILD_TYPE}")
message(STATUS "Shared libs       : ${BUILD_SHARED_LIBS}")
message(STATUS "Boost static libs : ${Boost_USE_STATIC_LIBS}")


#
# Boost libraries:
#
find_package(
  Boost
  1.50
  COMPONENTS 
    filesystem
    system
  REQUIRED
)


#
# CMake Modules:
#
include(cmake_modules/CompilerOptions.cmake)
include(cmake_modules/Rpath.cmake)
include(cmake_modules/Utils.cmake)


#
# Add subdirectories:
#
add_subdirectory(src)
add_subdirectory(doc)