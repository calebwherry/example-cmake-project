########################################
## \file   CMakeLists.txt
## \date   01/01/2014
## \brief  test-app: App CMake file.
########################################

# Set app name and app directory:
set(appName "TestApp")
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