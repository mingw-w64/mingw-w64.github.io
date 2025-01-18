# Ubuntu / Debian

## Installation

Install the 64bit C and C++ cross-compilers.

```console
$ sudo apt install g++-mingw-w64-x86-64 gcc-mingw-w64-x86-64
```

To check the version of the provided GCC and mingw-w64 via:

```console
$ apt-cache show gcc-mingw-w64-x86-64 | grep Version:
Version: 13.2.0-6ubuntu1+26.1  # GCC Version
$ apt-cache show mingw-w64-x86-64-dev | grep Version:
Version: 12.0.0-3  # Mingw-w64 Version
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

```console
$ x86_64-w64-mingw32-gcc hello.c -o hello.exe
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
