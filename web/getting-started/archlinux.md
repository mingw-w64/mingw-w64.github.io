# Arch Linux

## Installation

Install the 64bit C and C++ cross-compilers:

```console
$ sudo pacman -S mingw-w64-gcc
```

To check the version of the provided GCC and mingw-w64:

```console
$ pacman -Qi mingw-w64-gcc | grep Version
Version         : 14.2.0-3  # GCC Version
$ pacman -Qi mingw-w64-headers | grep Version
Version         : 12.0.0-1  # mingw-w64 Version
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

For installing wine, the multilib repo has to be enabled first. See the [Arch Wiki](https://wiki.archlinux.org/title/Official_repositories#multilib) for more information. After that is done:

```console
$ sudo pacman -S wine
```

```console
$ wine hello.exe
Hello, Windows!
```
