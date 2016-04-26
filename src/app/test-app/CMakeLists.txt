########################################
## \file   CMakeLists.txt
## \date   01/01/2014
## \brief  test-app: App CMake file.
########################################

# Set app name and app directory:
set(appName "test-app")
set(appDir "${CMAKE_CURRENT_LIST_DIR}")

# Create executable:
add_executable(${appName}
	"test-app.cpp"
)

# Link libs:
target_link_libraries(${appName} LINK_PUBLIC 
  TestPrint
)

# Install app:
install(TARGETS ${appName} RUNTIME DESTINATION bin)

# Add POST_BUILD step on windows to copy dll
if (WINDOWS AND BUILD_SHARED_LIBS)

add_custom_command(
  TARGET ${appName}
  POST_BUILD
  COMMAND
    ${CMAKE_COMMAND} -E copy_if_different
    "${CMAKE_BINARY_DIR}/src/lib/TestPrint/\$\(Configuration\)/TestPrint.dll"
    "$<TARGET_FILE_DIR:${appName}>"
  COMMENT Copying DLLs to EXE Build Directory
)

endif()