# MSYS2

## Installation

Install MSYS2 from the official website: https://www.msys2.org

After installation, open "MSYS2 UCRT64" from the Start menu and install the C
and C++ compiler:

```console
$ pacman -S mingw-w64-ucrt-x86_64-gcc
```

To check the installed GCC version:

To check the version of the provided GCC and mingw-w64:

```console
$ pacman -Qi mingw-w64-ucrt-x86_64-gcc | grep Version
Version         : 14.2.0-2  # GCC Version
$ pacman -Qi mingw-w64-ucrt-x86_64-headers | grep Version
Version         : 12.0.0.r473.gce0d0bfb7-1  # mingw-w64 Version
```

## Building

Creating and compiling a Windows executable:

```c
// hello.c
#include <stdio.h>

int main(void) {
    printf("Hello, Windows!\n");
    return 0;
}
```

```console
$ gcc hello.c -o hello.exe
```

## Testing

```console
$ ./hello.exe
Hello, Windows!
```
