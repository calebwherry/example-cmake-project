////////////////////////////////////////
// \file     test-app.cpp
// \date     01/01/2014
// \brief    test-app App
////////////////////////////////////////


//
// Local includes:
//
#include "TestPrint.hpp"


//
// Compiler includes:
//

// boost:
#include <boost/filesystem.hpp>

// std/STL:
#include <iostream>
#include <string>


//
// Namespaces:
//
namespace bfs = boost::filesystem;
namespace tp = test_print;
using namespace std;


//
// Main:
//
int main (int argc, char* argv[])
{

  // App print:
  string helloWorld = "Hello, world!";
  cout << helloWorld << endl;

  // Lib print:
  tp::testPrintLibFunction();

  // Path test:
  if (argc == 2)
  {
    // Check path information:
    bfs::path p(argv[1]);
    tp::printPathInfo(p);
  }
  else
  {
    cout << "Incorrect number of arguments given; only one is accepted." << endl;
  }

  // Exit:
  return 0;
}
