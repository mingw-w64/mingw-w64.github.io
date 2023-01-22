# to_string

**Q:**
I get some errors with C++11 to\_string when building/using GCC, what
gives?

**A:**
GCC 4.8.x and later supports std::to\_string and requires at least r5437
from the Mingw-w64 trunk SVN to support std::to\_string. The main change
in r5437 is that swprintf is now ISO complaint rather than MS specific.
This is the same behavior exhibited by recent Visual Studio releases.

To use the old behavior, use \_CRT\_NON\_CONFORMING\_SWPRINTFS or
\_swprintf instead. Note that setting \_CRT\_NON\_CONFORMING\_SWPRINTFS
when in C++11 mode will lead to undefined behavior.