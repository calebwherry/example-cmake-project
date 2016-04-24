########################################
## \file   CMakeLists.txt
## \date   01/01/2014
## \brief  Doc-level CMakeLists.txt
########################################


#
# Compile doxygen documentation:
#

# Find Doxygen:
find_package(Doxygen)

# Only process if doxygen was found:
if (DOXYGEN_FOUND)

  configure_file(${CMAKE_CURRENT_LIST_DIR}/Doxyfile.in ${PROJECT_BINARY_DIR}/Doxyfile @ONLY IMMEDIATE)
  add_custom_target(doc ALL
    ${DOXYGEN_EXECUTABLE} ${PROJECT_BINARY_DIR}/Doxyfile
    WORKING_DIRECTORY ${PROJECT_BINARY_DIR}
    COMMENT "Generating API documentation with Doxygen" VERBATIM
  )
  install(DIRECTORY ${PROJECT_BINARY_DIR}/doc/html DESTINATION doc)

else ()
  message(WARNING "Doxygen documentation could not be generated because Doxygen was not found on this system; skipping documentation creation.")
endif ()
