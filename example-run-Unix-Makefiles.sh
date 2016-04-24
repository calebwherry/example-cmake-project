#!/bin/sh

# Build project:
echo "-> Building project..."
./build.py --clean --build-type="Debug" --build-generator="Unix Makefiles" --static-build

# Run build binary:
echo "-> Running project binary..."
./build_Debug/local-install/bin/TestApp

# Exit:
exit 0
