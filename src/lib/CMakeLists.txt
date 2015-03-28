########################################
## \file   CMakeLists.txt
## \date   01/01/2014
## \brief  Main lib-level Cmake file.
########################################


#
# Library Rules
#

# Get all files/folders:
file(GLOB subDirs RELATIVE
  ${CMAKE_CURRENT_LIST_DIR}
  ${CMAKE_CURRENT_LIST_DIR}/*
)

# Iterate through and create each library for each sub folder:
foreach(subDir ${subDirs})

  # Must be a directory:
  if(IS_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/${subDir})

    # Set lib name and lib directory:
    set(libName ${subDir})
    set(libDir ${CMAKE_CURRENT_LIST_DIR}/${libName})

    # If a CMakeLists.txt file exists, include it here:
    # Note:
    #   For all libraries that we want compiled, there should be a
    #     CMakeLists.txt file in the directory. This will have compiler
    #     and library specific settings used below.
    if (EXISTS ${libDir}/CMakeLists.txt)

      # Include library CMakeLists.txt:
	    include(${libName}/CMakeLists.txt)

      # only compile if var set in above CMakeLists:
      if (${COMPILE_LIB})

        # Rules for compiling libraries:
        # Note:
        #   All variables used here should be defined in the CMakeLists.txt
        #     included above (or are CMake vars).

        # Create library:
        file(GLOB libSrcs RELATIVE ${libDir}
          ${libDir}/*.cpp ${libDir}/*/*.cpp
        )
        file(GLOB libHeaders RELATIVE ${libDir}
          ${libDir}/*.hpp ${libDir}/*.h
          ${libDir}/*/*.hpp ${libDir}/*/*.h
        )
        LIST_PREPEND(libSrcs ${libName})
        LIST_PREPEND(libHeaders ${libName})
        add_library(${libName} ${libSrcs})
        target_include_directories(${libName} PUBLIC ${libDir})
        set_target_properties(${libName} PROPERTIES COMPILE_FLAGS "${LIB_COMPILER_FLAGS}")

        # Link libs:
        foreach (libDepend ${LIB_LIBRARY_DEPENDS})

          # Check to see if lib coming back needs to be substituted again. If not, just link it directly:
          if ("${${libDepend}}" STREQUAL "")
            set(libDepend "${libDepend}")
          else()
            set(libDepend "${${libDepend}}")
          endif()

          target_link_libraries(${libName} LINK_PUBLIC ${libDepend})

        endforeach()

        # Install lib:
        install(TARGETS ${libName} DESTINATION lib)

        # Install headers:
        install(FILES ${libHeaders} DESTINATION include/${PROJECT_NAME}/${libName})

      else()
        message(STATUS "LIBS: Library '${libName}' compilation turned off; skipping.")
      endif()

    else()
      message(STATUS "LIBS: No CmakeLists.txt file for library '${libName}'; skipping.")
    endif()

	endif()

endforeach()
