# Meson

Meson is a multiplatform build system with good support for mingw-w64. See the
[official documentation](https://mesonbuild.com/) for more details.

## Detect mingw-w64 at Configuration Time

While it should be sufficient in most cases to use the preprocessor to detect
mingw-w64 at compile time, it can also be detected at configuration time if
necessary:

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

To cross compile a meson project for Windows while working on Linux:

* Install a Windows cross compiler on your Linux system
* Create or use a cross file that defines how meson should use the cross
  compiler
* Configure your project with the cross file

For detailed instructions, consult the [official meson
documentation](https://mesonbuild.com/Cross-compilation.html).

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

```console
$ meson setup builddir --cross-file cross-mingw64.txt
$ meson compile -C builddir
$ wine builddir/hello.exe
Hello, Windows!
```
