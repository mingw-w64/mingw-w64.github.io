# Building OpenSSL with mingw-w64

OpenSSL is an encryption library used in many open source projects to
provide stuff like HTTPS, ...

## Download available

There is a prebuilt package available from the mingw-w64 downloads
section, no need to build it yourself.

## How to Build

-   set up mingw-w64: [GeneralUsageInstructions](../general-usage-instructions.md)

-   set up MSYS: [MSYS](../msys.md)

-   get OpenSSL (v1.0.0 or later): <a href="http://openssl.org/source/"
    rel="nofollow">http://openssl.org/source/</a>

-   in the source directory from the MSYS shell:

        configure mingw64 [zlib[-shared]] [--prefix=/some/prefix]

    -   add zlib if you have zlib installed (there is a package in the
        External Binary Packages section in the mingw-w64 Downloads
        section.

    -   Add zlib-shared if you want to link with the zlib DLL.

    -   --prefix=/some/prefix will set the install directory

    -   type

        make  
        make check  
        make install