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
  // Test prints:
  cout << "Hello, world!" << endl;
  tp::TestPrint();

  // Exit:
  return 0;
}
