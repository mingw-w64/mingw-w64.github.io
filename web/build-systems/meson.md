# Meson

## Detect mingw-w64 at Configuration Time

```meson
# meson.build
cc = meson.get_compiler('c')
is_windows = host_machine.system() == 'windows'
is_mingw = is_windows and cc.get_define('__MINGW32__') != ''
if is_mingw
    message('Building with mingw-w64')
else
    message('Not building with mingw-w64')
endif
```

## Cross compiling on Linux

```c
// hello.c
#include <stdio.h>

int main(void) {
    printf("Hello, Windows!\n");
    return 0;
}
```

```ini
# cross-mingw64.txt
[host_machine]
system = 'windows'
cpu_family = 'x86_64'
cpu = 'x86_64'
endian = 'little'

[binaries]
c = 'x86_64-w64-mingw32-gcc'
cpp = 'x86_64-w64-mingw32-g++'
ar = 'x86_64-w64-mingw32-ar'
ld = 'x86_64-w64-mingw32-ld'
objcopy = 'x86_64-w64-mingw32-objcopy'
strip = 'x86_64-w64-mingw32-strip'
pkg-config = 'x86_64-w64-mingw32-pkg-config'
windres = 'x86_64-w64-mingw32-windres'
```

```meson
# meson.build
project('hello', 'c')
executable('hello', 'hello.c')
```

```console
$ meson setup builddir --cross-file cross-mingw64.txt
$ meson compile -C builddir
$ wine builddir/hello.exe
Hello, Windows!
```