@echo off

REM Build project:
echo "-> Building project..."
call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" x64
"%PYTHON%\python.exe build.py --clean --build-type="Debug" --build-generator="Visual Studio 14 2015 Win64" --static-build"

REM Run build binary:
echo "-> Running project binary..."
build_Debug\local-install\bin\TestApp

REM Exit:
timeout /t 10
exit 0