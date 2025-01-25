# CMake

CMake is a widely-used, cross-platform build system generator with excellent support for mingw-w64. See the [official documentation](https://cmake.org/documentation/) for more information.

## Detect mingw-w64 at Configuration Time

While preprocessor definitions can be used to detect mingw-w64 at compile time, CMake provides variables to detect it during configuration:

```cmake
# CMakeLists.txt
if(MINGW)
    message(STATUS "Building with mingw-w64")
else()
    message(STATUS "Not building with mingw-w64")
endif()
```

## Cross compiling on Linux

To cross compile a CMake project for Windows while working on Linux:

* Install a Windows cross compiler on your Linux system
* Create or use a toolchain file that defines how CMake should use the cross compiler
* Configure your project with the toolchain file

For detailed instructions, consult the [official CMake documentation](https://cmake.org/cmake/help/book/mastering-cmake/chapter/Cross%20Compiling%20With%20CMake.html).

```cmake
# toolchain-mingw64.cmake
set(CMAKE_SYSTEM_NAME Windows)
set(CMAKE_SYSTEM_PROCESSOR x86_64)

# specify the cross compiler
set(CMAKE_C_COMPILER x86_64-w64-mingw32-gcc)
set(CMAKE_CXX_COMPILER x86_64-w64-mingw32-g++)
set(CMAKE_RC_COMPILER x86_64-w64-mingw32-windres)

# where is the target environment
set(CMAKE_FIND_ROOT_PATH /usr/x86_64-w64-mingw32)

# search for programs in the build host directories
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
# for libraries and headers in the target directories
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
```

```console
$ cmake -B build -DCMAKE_TOOLCHAIN_FILE=toolchain-mingw64.cmake
$ cmake --build build
$ wine build/hello.exe
Hello, Windows!
```
