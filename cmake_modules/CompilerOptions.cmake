########################################
## \file   compiler_options.cmake
## \date   01/01/2014
## \brief  Compiler options
########################################


#
# OS-specific compiler definitions:
#
if (MAC)
  add_definitions(-DUNIX -DMAC)
elseif (LINUX)
  add_definitions(-DUNIX -DLINUX)
elseif (WINDOWS)
  add_definitions(-DWINDOWS)
endif()


#
# Project-wide compiler flags:
#
if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")

  # Check version. If empty, warn. If too old, error out:
  if ("${CMAKE_CXX_COMPILER_VERSION}" STREQUAL "")
    message(WARNING "GCC compiler version is unknown, proceed at your own risk!")
  elseif (CMAKE_CXX_COMPILER_VERSION VERSION_LESS 4.9)
    message(FATAL_ERROR "GCC compiler version must be at least 4.9 (current version: ${CMAKE_CXX_COMPILER_VERSION})!")
  endif()

  # Set compiler CMake vars:
  set(GCC 1)
  set(CLANG 0)
  set(MSVC 0)
  set(INTEL 0)
  set(COMPILER "GCC")
  
  # Add compiler-specific definitions:
  add_definitions(-DGCC)
  
  # Set compiler/linker specific flags:
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
  #set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")
  #set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS}")

elseif (CMAKE_CXX_COMPILER_ID MATCHES Clang) # Matches used here since Apple's clang is 'AppleClang' and normal is 'Clang'

  # Check version. If empty, warn. If too old, error out:
  if ("${CMAKE_CXX_COMPILER_VERSION}" STREQUAL "")
    message(WARNING "Clang compiler version is unknown, proceed at your own risk!")
  elseif (CMAKE_CXX_COMPILER_VERSION VERSION_LESS 3.7)
    message(FATAL_ERROR "Clang compiler version must be at least 3.7 (current version: ${CMAKE_CXX_COMPILER_VERSION})!")
  endif()

  # Set compiler CMake vars:
  set(GCC 0)
  set(CLANG 1)
  set(MSVC 0)
  set(INTEL 0)
  set(COMPILER "CLANG")
  
  # Add compiler-specific definitions:
  add_definitions(-DCLANG)
  
  # Set compiler/linker specific flags:
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
  #set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")
  #set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS}")

elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")

  # Check version. If empty, warn. If too old, error out:
  if ("${CMAKE_CXX_COMPILER_VERSION}" STREQUAL "")
    message(WARNING "MSVC compiler version is unknown, proceed at your own risk!")
  elseif (CMAKE_CXX_COMPILER_VERSION VERSION_LESS 19.0)
    message(FATAL_ERROR "MSVC compiler version must be at least 19.0 (current version: ${CMAKE_CXX_COMPILER_VERSION})!")
  endif()

  # Set compiler CMake vars:
  set(GCC 0)
  set(CLANG 0)
  set(MSVC 1)
  set(INTEL 0)
  set(COMPILER "MSVC")
  
  # Add compiler-specific definitions:
  add_definitions(-DMSVC)
  
  # Set compiler/linker specific flags:
  # Note: Using defaults.
  #set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  #set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")
  #set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS}")

elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Intel")

  # Check version. If empty, warn. If too old, error out:
  if ("${CMAKE_CXX_COMPILER_VERSION}" STREQUAL "")
    message(WARNING "Intel compiler version is unknown, proceed at your own risk!")
  elseif (CMAKE_CXX_COMPILER_VERSION VERSION_LESS 15.0)
    message(FATAL_ERROR "Intel compiler version must be at least 15.0 (current version: ${CMAKE_CXX_COMPILER_VERSION})!")
  endif()

  # Set compiler CMake vars:
  set(GCC 0)
  set(CLANG 0)
  set(MSVC 0)
  set(INTEL 1)
  set(COMPILER "INTEL")
  
  # Add compiler-specific definitions:
  add_definitions(-DINTEL)
  
  # Set compiler/linker specific flags:
  # Note: Using defaults.
  #set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  #set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")
  #set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS}")

else()
  message(WARNING "The '${CMAKE_CXX_COMPILER_ID}' compiler is untested and unsupported, continue at your own risk!")
endif()
