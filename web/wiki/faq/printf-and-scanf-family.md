# printf and scanf family


Some functions provided by Microsoft does not work as described in C99
specifications. For example the function `vsnprintf()` does not return
the number of characters that would have been printed but only `-1` if
the formatted string does not fit in the given buffer.

Mingw-w64 provides possibility to assume that ANSI I/O standards are
preferred over Microsoft's. This is enabled by

      #define __USE_MINGW_ANSI_STDIO 1

before including any system headers, or the equivalent command-line
option `-D__USE_MINGW_ANSI_STDIO` of GCC and Clang. It was once possible
to define `__USE_MINGW_ANSI_STDIO` as zero to disable this feature; such
use is now discouraged.

By using mingw-w64's trunk version (25th January 2011 or later) you will
have support for wide-character `printf()` routines, too. They are also
enabled by defining `__USE_MINGW_ANSI_STDIO` as described above.

`scanf()` routines have been available since 4th Feburary 2011.
