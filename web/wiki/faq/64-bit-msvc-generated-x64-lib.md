# 64 bit MSVC-generated x64 .lib

**Q:**  
Why crashes my 64 bit program when using a MSVC-generated x64 import
library?

**A:**  
Linking using an MSVC-generated x64 `*.lib` file is *not* supported.  
Yes the x86 variant is supported but x64 is not, and yes binutils will
be silent  
and link but will output an all wrong binary. See, e.g. a thread here:  
<https://sourceforge.net/projects/mingw-w64/forums/forum/723797/topic/3882579>

If you generate a binutils-compatbile `*.a` file by using gendef on the
dll  
and then compiling it, like:

    gendef wpcap.dll   
    dlltool --as-flags=--64 -m i386:x86-64 -k --output-lib libwpcap.a --input-def wpcap.def

... then things will work.
