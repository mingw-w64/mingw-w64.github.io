# MSYS2 (Clang/LLVM)

## Installation

Install MSYS2 from the official website: https://www.msys2.org

After installation, open "MSYS2 CLANG64" from the Start menu and install the C
and C++ compiler:

```console
$ pacman -S mingw-w64-clang-x86_64-clang
```

To check the version of the provided Clang and mingw-w64:

```console
$ pacman -Qi mingw-w64-clang-x86_64-clang | grep Version
Version         : 19.1.7-1  # Clang Version
$ pacman -Qi mingw-w64-clang-x86_64-headers | grep Version
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
$ clang hello.c -o hello.exe
```

## Testing

```console
$ ./hello.exe
Hello, Windows!
```
