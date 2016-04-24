////////////////////////////////////////
// \file    TestPrint.hpp
// \date    01/01/2015
// \brief   TestPrint lib header.
////////////////////////////////////////

#pragma once


//
// API entry point:
//
#ifdef WINDOWS
#define PUBLIC_API __declspec(dllexport)
#else
#define PUBLIC_API
#endif


///
/// Library namespace
///
namespace test_print
{


/// Test print
PUBLIC_API void TestPrint();


} // namespace test_print