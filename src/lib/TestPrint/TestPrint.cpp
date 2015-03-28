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

// std/STL:
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

  // Print path info:
  void printPathInfo(const bfs::path& p)
  {

    // Does p actually exist:
    if (exists(p))
    {
      // Figure out type of p:
      if (is_regular_file(p))
      {
        cout << p << " is a regular file (size: " << file_size(p) << " bytes)." << endl;
      }
      else if (is_directory(p))
      {
        cout << p << " is a directory." << endl;
      }
      else
      {
        cout << p << " exists, but is neither a regular file nor a directory." << endl;
      }

    }
    else
    {
      cout << p << " does not exist." << endl;
    }

  }

} // namespace test_print
