#!/usr/bin/env python
########################################
## \file   build.py
## \date   01/01/2014
## \brief  Automated build script.
########################################


#
# Global imports:
#
from __future__ import print_function

import multiprocessing, string, subprocess
from time import time
from colorama import init, Fore
from sys import exit
from os import remove


#
# Global start time:
#
startTime = time()


#
# Calculate elapsed time:
#
def elapsedTime(time1, time2):

  elapsedTime = time2 - time1
  totalHours = int(elapsedTime / 3600)
  totalMinutes = int(elapsedTime / 60) % 60
  totalSeconds = elapsedTime % 60

  if totalHours != 0:
    elapsedTimeString = "{:d} hours, {:d} minutes, & {:.4f} seconds.".format(totalHours, totalMinutes, totalSeconds)
  elif totalMinutes != 0:
    elapsedTimeString = "{:d} minutes & {:.4f} seconds.".format(totalMinutes, totalSeconds)
  else:
    elapsedTimeString = "{:.4f} seconds.".format(totalSeconds)

  return elapsedTimeString



#
# Print log to stdout:
#
def displayLog(log):

  print('')
  print(Fore.MAGENTA + '#############################')
  print(Fore.MAGENTA + 'Dumping log file: ' + log.name)
  print(Fore.MAGENTA + '#############################')
  print('')

  # Open file and print it to stdout:
  with open(log.name, 'r') as fin:
    print(fin.read())

  print('')
  print(Fore.MAGENTA + '#############################')
  print(Fore.MAGENTA + 'End log dump.')
  print(Fore.MAGENTA + '#############################')
  print('')



#
# Execute system call:
#
def sysCall(cmds, log, pad="", shellExec=False):

  # Print command and run:
  print(pad + "Running '" + " ".join(cmds) + "'...", end=' ')

  beginTime = time()
  returnCode = subprocess.call(cmds, shell=shellExec, stdout=log, stderr=subprocess.STDOUT)
  endTime = time()

  if returnCode != 0:
    print(Fore.RED + 'ERROR!!! Please see log output below!')
    displayLog(log)
    completeScript(1)
  print(Fore.GREEN + 'done! ' + elapsedTime(beginTime,endTime))



#
# Complete script:
#
def completeScript(exitCode=0):

  # Elapsed time:
  stopTime = time()

  # Display execution time:
  print('Execution time: ' + elapsedTime(startTime,stopTime))
  print('')

  # Script completion output:
  if exitCode == 0:
    print(Fore.GREEN + 'Script completed successfully: {:d}.'.format(exitCode))
  else:
    print(Fore.RED + 'Script completed UNsuccessfully: {:d}.'.format(exitCode))
  print('')

  # Exit:
  exit(exitCode)



#
# UNIX build:
#
def unixBuild(log, args):

  print('')
  print('UNIX build starting...')

  # Execute build commands:
  sysCall(["make", "-j"+str(args.num_cpus)], log, "\t")
  #sysCall(["make", "-j"+str(args.num_cpus), "test"], log, "\t")
  sysCall(["make", "-j"+str(args.num_cpus), "doc"], log, "\t")
  sysCall(["make", "-j"+str(args.num_cpus), "install"], log, "\t")

  print('UNIX build complete!')
  print('')



#
# Windows build:
#
def windowsBuild(log, args):

  print('')
  print('Windows build starting...')

  # Execute build commands:
  sysCall(["msbuild", "ALL_BUILD.vcxproj"], log, "\t")
  #sysCall(["msbuild", "RUN_TESTS.vcxproj"], log, "\t")
  sysCall(["msbuild", "ZERO_CHECK.vcxproj"], log, "\t")
  sysCall(["msbuild", "INSTALL.vcxproj"], log, "\t")

  print('Windows build complete!')
  print('')



#
# Main:
#
if __name__ == "__main__":

  # Imports:
  import argparse
  from sys import argv
  from os import path, getcwd, mkdir, chdir
  from platform import system
  from datetime import datetime
  from shutil import rmtree
  from glob import glob


  #
  # Argument parsing:
  #
  parser = argparse.ArgumentParser()
  parser.add_argument("-b", "--build-type", help="Build type (default: Debug).", choices=["Debug","Release","RelWithDebInfo","MinSizeRel"], default="Debug")
  parser.add_argument("-c", "--cleanall", help="Remove build directory in current working directory matching 'build_${BUILD_TYPE}' then continue build", action="store_true")
  parser.add_argument("-g", "--build-generator", help="Build generator type that CMake produces, see 'cmake --help' for the available options on this platform (default: CMake decides based on system settings).", type=str, default="")
  parser.add_argument("-i", "--install-prefix", help="Prefix for the install directory.", type=str, default="")
  parser.add_argument("-j", "--num-cpus", help="Number of CPUs for parallel builds (default: number of CPUs on machine)", type=int, default=multiprocessing.cpu_count())
  parser.add_argument("-l", "--log-display", help="Display build log to stdout.", action="store_true")
  parser.add_argument("-n", "--build-dir-name", help="Name of the build directory created (default: 'build')", type=str, default="build")
  parser.add_argument("-r", "--remove-build", help="Remove current build directory after completion.", action="store_true")
  parser.add_argument("-s", "--static-libs", help="Build and link libraries static instead of shared.", action="store_true")
  args = parser.parse_args()


  #
  # Init colorama:
  #
  init(autoreset=True)


  #
  # Build script init output:
  #
  print('')
  print(Fore.GREEN + '######################')
  print(Fore.GREEN + 'Automated Build Script')
  print(Fore.GREEN + '######################')
  print('')

  # Get timestamp:
  timeStamp = datetime.fromtimestamp(time()).strftime('%Y-%m-%d_%H-%M-%S')

  # Get current path:
  currentPath = path.abspath(getcwd())

  # Get script path:
  # NOTE:
  #   This SHOULD be cross-platform but some people say it isn't because of
  #   the argv... I have yet to come across a situation where this fails so
  #   I'm leaving it. I believe when it fails is if you have this in a module
  #   therefore there is no argv define. However, in this case, this script
  #   will always be run from the commnad line so we should not run into any
  #   issues.
  scriptPath = path.abspath(path.dirname(argv[0]))

  # Get OS:
  localOS = system()

  # Remove build directories if clean specified:
  if args.cleanall:

    # build dir:
    print("Removing build directory matching 'build/':")
    buildDirs = glob('build/')
    buildDirs = filter(path.isdir, buildDirs)
    for dir in buildDirs:
      print(Fore.RED + "\t" + dir)
      rmtree(dir)
    print(Fore.GREEN + 'done!')
    print('')

  # Create build directories:
  buildRoot = path.join(currentPath, args.build_dir_name)
  buildDir = path.join(buildRoot, 'build-files')

  # Try and create build directory. If it exists, use dir and rebuild.
  reBuild = False;
  try:
    mkdir(buildRoot)
    mkdir(buildDir)
  except:
    reBuild = True;
    print("Build directory '" + args.build_dir_name + "' already exists; re-running build process.")
    print('')

  # Diplay build directory to screen:
  print('Build location: ' + Fore.MAGENTA + buildRoot + "\n")

  # Create install directory if prefix was not supplied:
  if args.install_prefix == "":
    installDir = path.join(buildRoot, 'install-files')
    if not reBuild:
      mkdir(installDir)
  else:
    installDir = path.join(args.install_prefix)

  # Set library build type:
  if args.static_libs:
    sharedLibs = "OFF"
  else:
    sharedLibs = "ON"

  # Move into build directory:
  chdir(buildDir)

  # Create logfile:
  logFile = path.join(buildRoot, 'build.log')
  log = open(logFile, 'w');

  # Check number of cpus:
  if args.num_cpus <= 2:
    args.num_cpus = 1
  elif (args.num_cpus > 2) and (args.num_cpus <= 4):
    args.num_cpus = args.num_cpus - 1
  elif (args.num_cpus > 5) and (args.num_cpus <= 10):
    args.num_cpus = args.num_cpus - 2
  else:
    args.num_cpus = args.num_cpus - 4

  # Build up CMake command based on CLI options:
  cmakeCmd = [
    "cmake", scriptPath,
    "-DCMAKE_INSTALL_PREFIX='" + installDir + "'",
    "-DCMAKE_BUILD_TYPE=" + args.build_type,
    "-DBUILD_SHARED_LIBS:BOOL=" + sharedLibs,
    "-DCMAKE_INSTALL_SO_NO_EXE=0"
  ]
  if (args.build_generator != ""):
    cmakeCmd.append("-G" + args.build_generator)

  # On all platforms, we at least have to run cmake first to get build files:
  sysCall(cmakeCmd, log)

  # Execute build based on platform from this point on:
  if localOS == 'Linux' or localOS == 'Darwin':
    unixBuild(log, args)
  elif localOS == 'Windows':
    windowsBuild(log, args)
  else:
    print(Fore.RED + '**ERROR**: OS platform "' + localOS + '" not recognized; aborting!')
    completeScript(1)

  # Display log if cmd argument set:
  if args.log_display:
    displayLog(log)

  # Close log file:
  log.close()

  # Remove build directory if flag set
  chdir(scriptPath)
  if args.remove_build:
    print('Removing current build directory...', end=' ')
    rmtree(buildRoot)
    print(Fore.GREEN + 'done!')
    print('')

  # Exit cleanly:
  completeScript()
