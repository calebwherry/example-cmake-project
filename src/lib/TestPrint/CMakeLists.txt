########################################
## \file   CMakeLists.txt
## \date   01/01/2014
## \brief  Test Lib CMake file.
########################################

# Set lib name and lib directory:
set(libName "TestPrint")
set(libDir "${CMAKE_CURRENT_LIST_DIR}")

# Explicitly specify source/headers:
set(Headers
	"TestPrint.hpp"
)

set(Sources
	"TestPrint.cpp"
)

# Create source group:
source_group("Headers" FILES ${Headers})
source_group("Sources" FILES ${Sources})

# Create library:
add_library(${libName}
	${Headers}
	${Sources}
)

# Includes and link libs:
target_include_directories(${libName} PUBLIC ${libDir})
#target_link_libraries(${libName} LINK_PUBLIC ${Boost_LIBRARIES})

# Install artifacts:
install(TARGETS ${libName} DESTINATION lib)
install(FILES ${Headers} DESTINATION include)