# Debian / Ubuntu

## Installation

Install the 64bit C and C++ cross-compilers.

=== "msvcrt"

    ```console
    $ sudo apt install g++-mingw-w64-x86-64 gcc-mingw-w64-x86-64
    ```

=== "ucrt"

    ```console
    $ sudo apt install g++-mingw-w64-ucrt64 gcc-mingw-w64-ucrt64
    ```

    **Note:** UCRT targeting cross compilers are currently only available in Debian 13 (trixie).

To check the version of the provided GCC and mingw-w64 via:

=== "msvcrt"

    ```console
    $ apt-cache show gcc-mingw-w64-x86-64 | grep Version:
    Version: 13.3.0-12+26.7  # GCC Version
    $ apt-cache show mingw-w64-x86-64-dev | grep Version:
    Version: 12.0.0-5  # mingw-w64 Version
    ```

=== "ucrt"

    ```console
    $ apt-cache show gcc-mingw-w64-ucrt64 | grep Version:
    Version: 13.3.0-12+26.7  # GCC Version
    $ apt-cache show mingw-w64-ucrt64-dev | grep Version:
    Version: 12.0.0-5  # mingw-w64 Version
    ```

## Building

Cross compiling a Windows executable:

```c
// hello.c
#include <stdio.h>

int main(void) {
    printf("Hello, Windows!\n");
    return 0;
}
```

=== "msvcrt"

    ```console
    $ x86_64-w64-mingw32-gcc hello.c -o hello.exe
    ```

=== "ucrt"

    ```console
    $ x86_64-w64-mingw32ucrt-gcc hello.c -o hello.exe
    ```

## Testing

Testing on Linux using Wine:

```console
$ sudo apt install wine
```

```console
$ wine hello.exe
Hello, Windows!
```
