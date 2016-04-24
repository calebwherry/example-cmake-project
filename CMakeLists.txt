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
# Some variables need to be set before 'project' is defined:
#

# Build type:
if (DEFINED CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "${CMAKE_BUILD_TYPE}" CACHE STRING "Choose the type of build, options are: Debug, Release, RelWithDebInfo, or MinSizeRel." FORCE)
else()
  # Default is Debug:
  set(CMAKE_BUILD_TYPE "Debug" CACHE STRING "Choose the type of build, options are: Debug, Release, RelWithDebInfo, or MinSizeRel." FORCE)
endif()

# Shared libs:
if (DEFINED BUILD_SHARED_LIBS)
  set(BUILD_SHARED_LIBS ${BUILD_SHARED_LIBS} CACHE BOOL "Choose to build libraries as shared or not" FORCE)
else()
  set(BUILD_SHARED_LIBS ON CACHE BOOL "Choose to build libraries as shared or not" FORCE)
endif()

# Set specific cmake policies:
cmake_policy(SET CMP0054 NEW) # Will eventually be turned on by default by CMake. For now it suppresses unneeded warnings for variable dereferencing.


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
# Figure out OS:
#
if (APPLE)

  set(UNIX 1)
  set(MAC 1)
  set(LINUX 0)
  set(WINDOWS 0)
  
  set(OS_BASE "unix")
  set(OS "mac")
  set(OS_FULL "${OS_BASE}/${OS}")
  
elseif (UNIX)

  set(UNIX 1)
  set(MAC 0)
  set(LINUX 1)
  set(WINDOWS 0)
  
  set(OS_BASE "unix")
  set(OS "linux")
  set(OS_FULL "${OS_BASE}/${OS}")
  
elseif (WIN32)

  set(UNIX 0)
  set(MAC 0)
  set(LINUX 0)
  set(WINDOWS 1)
  
  set(OS_BASE "windows")
  set(OS "windows")
  set(OS_FULL "${OS}")
  
else()
  message(FATAL_ERROR "Unknown OS, cannot continue; aborting.")
endif()


#
# Calulate bit-size to set platform:
#
math(EXPR BITS "8*${CMAKE_SIZEOF_VOID_P}")
if ("${BITS}" STREQUAL "64")
  set(PLATFORM "x64")
  set(64BIT 1)
elseif ("${BITS}" STREQUAL "32")
  set(PLATFORM "x32")
  set(64BIT 0)
else()
  message(FATAL_ERROR "Unknown platform (bits=${BITS}), cannot continue; aborting.")
endif()


#
# CMake Modules:
#
include(cmake_modules/CompilerOptions.cmake)
#include(cmake_modules/Rpath.cmake)
include(cmake_modules/Utils.cmake)


#
# Print useful CMake info:
#
message(STATUS "Project           : ${PROJECT_NAME}")
message(STATUS "Project version   : ${${PROJECT_NAME}_VERSION}")
message(STATUS "Build type        : ${CMAKE_BUILD_TYPE}")
message(STATUS "Shared libs       : ${BUILD_SHARED_LIBS}")
message(STATUS "OS                : ${OS_FULL}")
message(STATUS "Platform          : ${PLATFORM}")
message(STATUS "Compiler          : ${COMPILER}")


#
# Add subdirectories:
#
add_subdirectory(src)
add_subdirectory(doc)