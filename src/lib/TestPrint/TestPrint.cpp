////////////////////////////////////////
// \file    TestPrint.cpp
// \date    01/01/2015
// \brief   TestPrint lib implementation.
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
// Namespaces
//
using namespace std;


//
// Library namespace:
//
namespace test_print
{

  // Test lib function:
  void testPrintLibFunction()
  {
    string libHelloWorld = "Hello, world! (From the TestPrint library)";
    cout << libHelloWorld << endl;
  }

} // namespace test_print
