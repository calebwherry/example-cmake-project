########################################
## \file   CMakeLists.txt
## \date   01/10/2014
## \brief  Main app-level Cmake file.
########################################


#
# Application Rules
#

# Get all files/folders:
file(GLOB subDirs RELATIVE
  ${CMAKE_CURRENT_LIST_DIR}
  ${CMAKE_CURRENT_LIST_DIR}/*
)

# Iterate through and create each app for each sub folder:
foreach(subDir ${subDirs})

  # Must be a directory:
  if (IS_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/${subDir})
   
    # Set app name and app directory:
    set(appName ${subDir})
    set(appDir ${CMAKE_CURRENT_LIST_DIR}/${appName})
 
    # If a CMakeLists.txt file exists, include it here:
    # Note:
    #   For all applications that we want compiled, there should be a 
    #     CMakeLists.txt file in the directory. This will have compiler
    #     and application specific settings used below.
    if (EXISTS ${appDir}/CMakeLists.txt)

      # Include app CMakeLists.txt:
	    include(${appName}/CMakeLists.txt)

      # Only compile if var set in above CMakeLists:
      if (${COMPILE_APP})

        # Rules for compiling applications:
        # Note:
        #   All variables used here should be defined in the CMakeLists.txt
        #     included above (or are CMake vars).

        # Create executable:
        file(GLOB appSrcs RELATIVE ${appDir} ${appDir}/*.cpp)
        LIST_PREPEND(appSrcs ${appName})
        add_executable(${appName} ${appSrcs})
        set_target_properties(${appName} PROPERTIES COMPILE_FLAGS "${APP_COMPILER_FLAGS}")

        # Link libs:
        foreach (libDepend ${APP_LIBRARY_DEPENDS})

          # Check to see if lib coming back needs to be substituted again. If not, just link it directly:
          if ("${${libDepend}}" STREQUAL "")
            set(libDepend "${libDepend}")
          else()
            set(libDepend "${${libDepend}}")
          endif()

          target_link_libraries(${appName} LINK_PUBLIC ${libDepend})

        endforeach()

        # Install app:
        install(TARGETS ${appName} RUNTIME DESTINATION bin)

      else()
        message(STATUS "APPS: Application '${appName}' compilation turned off; skipping.")
      endif()

    else()
      message(STATUS "APPS: No CmakeLists.txt file for application '${appName}'; skipping.")
    endif()

	endif()

endforeach()
