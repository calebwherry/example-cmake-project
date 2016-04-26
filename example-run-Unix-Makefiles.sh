#!/bin/sh

# Build project:
echo "-> Building project..."
./build.py --clean --build-type="Debug" --build-generator="Unix Makefiles"

# Run build binary:
echo "-> Running project binary..."
./build_Debug/build/src/app/test-app/test-app

# Exit:
exit 0
