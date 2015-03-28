########################################
## \file   CMakeLists.txt
## \date   01/01/2014
## \brief  Main project Cmake file.
########################################


#
# Minimum CMake version:
#
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)


#
# Constants:
#
set(DEBUG "DEBUG")
set(RELEASE "RELEASE")


#
# Project Properties:
#
project(skeleton-cpp-project CXX C)
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
  set(CMAKE_BUILD_TYPE ${DEBUG} CACHE STRING "Build type." FORCE)
else()
  string(TOUPPER ${CMAKE_BUILD_TYPE} buildType)
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
message(STATUS "Project Version: ${${PROJECT_NAME}_VERSION}")
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "Shared libs: ${BUILD_SHARED_LIBS}")
message(STATUS "Boost Static libs: ${Boost_USE_STATIC_LIBS}")


#
# Boost libraries:
#
find_package(
  Boost
  1.50.0
  COMPONENTS 
    filesystem
    system
  REQUIRED
)


#
# Project-level Compiler flags:
#
if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")

  # Check version. If empty, warn. If too old, error out:
  if ("${CMAKE_CXX_COMPILER_VERSION}" STREQUAL "")
    message(WARNING "GCC compiler version is unknown, proceed at your own risk!")
  elseif (CMAKE_CXX_COMPILER_VERSION VERSION_LESS 4.8)
    message(FATAL_ERROR "GCC compiler version must be at least 4.8 (current version: ${CMAKE_CXX_COMPILER_VERSION})!")
  endif()

  # Set compiler specific flags:
  set(CMAKE_CXX_FLAGS_DEBUG "-Wall -ggdb -std=c++11")
  set(CMAKE_CXX_FLAGS_RELEASE "-w -O3 -std=c++11")

  # Warnings to ignore during C++ debug build:
  set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wno-format-extra-args")

elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")

  # Check version. If empty, warn. If too old, error out:
  if ("${CMAKE_CXX_COMPILER_VERSION}" STREQUAL "")
    message(WARNING "Clang compiler version is unknown, proceed at your own risk!")
  elseif (CMAKE_CXX_COMPILER_VERSION VERSION_LESS 3.6)
    message(FATAL_ERROR "Clang compiler version must be at least 3.6 (current version: ${CMAKE_CXX_COMPILER_VERSION})!")
  endif()

  # Set compiler/linker specific flags:
  set(CMAKE_CXX_FLAGS_DEBUG "-Wall -ggdb -std=c++11 -stdlib=libc++")
  set(CMAKE_CXX_FLAGS_RELEASE "-w -O3 -std=c++11 -stdlib=libc++")

else()
  message(WARNING "The '${CMAKE_CXX_COMPILER_ID}' compiler is untested and unsupported, continue at your own risk!")
endif()


#
# RPATH properties:
#
set(CMAKE_NO_BUILTIN_CHRPATH on)
set(CMAKE_SKIP_BUILD_RPATH false)
set(CMAKE_BUILD_WITH_INSTALL_RPATH false)
set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH true)
list(FIND CMAKE_PLATFORM_IMPLICIT_LINK_DIRECTORIES "${CMAKE_INSTALL_PREFIX}/lib" isSystemDir)
if("${isSystemDir}" STREQUAL "-1")
  set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
endif()


#
# Include other cmake functions:
#
include(cmake/utils.cmake)


#
# Add subdirectories:
#
add_subdirectory(src)
add_subdirectory(doc)
