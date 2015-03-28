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
#include <iostream>
#include <string>


//
// Namespaces:
//
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

  // Exit:
  return 0;
}
