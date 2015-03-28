////////////////////////////////////////
// \file    TestPrint.hpp
// \date    01/01/2015
// \brief   TestPrint lib header.
////////////////////////////////////////


//
// Include guards:
//
#ifndef TESTPRINT_H
#define TESTPRINT_H


//
// Local includes:
//
////


//
// Compiler includes:
//
#include <boost/filesystem.hpp>


//
// Namespaces
//
namespace bfs = boost::filesystem;


//
// Library namespace:
//
namespace test_print
{

  // Test function:
  void testPrintLibFunction();

  // Print path info:
  void printPathInfo (
    const bfs::path&
  );

} // namespace test_print

#endif // TESTPRINT_H
