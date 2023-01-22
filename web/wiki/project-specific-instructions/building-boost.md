# Building Boost

Boos is a collection of libraries that are very respected in the C++
community. Large portions are to be included in the next C++ standard.

## How to build

-   set up mingw-w64: [GeneralUsageInstructions](../general-usage-instructions.md)

-   [Download Boost
    Sources](https://sourceforge.net/projects/boost/files/boost/) (the
    filename should look like "boost\_1\_43\_0.zip"

-   [Download Boost
    Jam](http://sourceforge.net/projects/boost/files/boost-jam/) (the
    filename should look like "boost-jam-3.1.18.zip")

-   extract Boost sources to C:\\Boost-src so that INSTALL is located in
    C:\\Boost-src.

-   extract bjam.exe and place it somewhere in C:\\Boost-src.

-   run the following command:

        bjam --toolset=gcc --build-dir=C:\ --build-type=complete

This will create a directory C:\\boost and build there. Some libraries
fail to build, feel free to submit patches to Boost devs.

NOTE: for x64, some parts are not supported. Contact Boost devs for
support. With boost version 1.44, try using the additional bjam option
"define=BOOST\_USE\_WINDOWS\_H" this will build additional parts (e.g.
threads) of boost.