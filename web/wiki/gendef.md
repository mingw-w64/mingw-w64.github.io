# gendef

gendef is a tool which generate def files from DLLs. A def file is a
list of symbols exported by a DLL. The primary use of this tool is to
allow creation of a import library of DLLs created by non-GCC compilers.
It can handle both x86 (win32) and amd64 (win64) executables.

It has almost the same function as pexports?. However, unlike pexports,
gendef scans and attempts to decode the dll file to find out relevant
details such as call convention used. It will try to append the @n to
symbols detected as using stdcall?.

## Usage

To dump a def file of a DLL use "gendef mydll.dll". A def file by the
name of "mydll.def" should be created. To print the exports to stdout
like pexports, add the "-" option "gendef - mydll.dll". For additional
help, use "gendef -h".

On 32b DLL one expects to get 'found PE-image' and with 64b 'found
PE+-image'. If this is not the case you probably got wrong dll file.

## Getting gendef

Easiest way to get gendef is to browse the source and download partition
of the source tree as single package. You can find the gendef tool under
trunk/mingw-w64-tools or you can use
[this](http://mingw-w64.svn.sourceforge.net/viewvc/mingw-w64/trunk/mingw-w64-tools/gendef/?view=tar)
direct link.

Compiling is easy. Create build directory (mkdir debug) and run
configure ('../configure') from there with options you want (like
'--prefix=$HOME/'). Type './configure -h' for more help. After configure
is done you can compile the tool with command 'make' and install the
binary with 'make install'.

## Known Issues

### void Functions

For win32 DLLs, gendef cannot detect if a function exported by a DLL is
using stdcall or cdecl? if it is a void type function. This is reasoned
by the similar stack? unwind prologue at the end of the function. If it
is certain a function is an stdcall function with a @0 suffix, use the
"-a" option to make gendef assume void functions are stdcall functions.
Win64 executables are not affected, there is only a single call
convention in use.

To work around this, use gendef to generate .def files from the DLL
dependencies first. gendef will read other def files found in the
working directory to determine the call conventions used. For example,
you should generate the def files from ntdll.dll and kernel32.dll before
trying to use gendef on msvcrt.dll.