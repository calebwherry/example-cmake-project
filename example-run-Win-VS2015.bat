@echo off
call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" x64
python build.py --clean --build-type="Debug" --build-generator="Visual Studio 14 2015 Win64"
pause