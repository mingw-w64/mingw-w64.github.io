# Fedora

## Installation

Install the 64bit C and C++ cross-compilers:

=== "msvcrt"

    ```console
    $ sudo dnf install mingw64-gcc-c++
    ```

=== "ucrt"

    ```console
    $ sudo dnf install ucrt64-gcc-c++
    ```

To check the version of the provided GCC and mingw-w64:

=== "msvcrt"

    ```console
    $ dnf info --installed mingw64-gcc | grep Version
    Version      : 14.2.1  # GCC Version
    $ dnf info --installed mingw64-crt | grep Version
    Version      : 12.0.0  # mingw-w64 Version
    ```

=== "ucrt"

    ```console
    $ dnf info --installed ucrt64-gcc | grep Version
    Version      : 14.2.1  # GCC Version
    $ dnf info --installed ucrt64-crt | grep Version
    Version      : 12.0.0  # mingw-w64 Version
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
$ sudo dnf install wine
```

```console
$ wine hello.exe
Hello, Windows!
```
