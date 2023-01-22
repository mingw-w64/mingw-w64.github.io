# libstdc++ build failures

The reason for this failure is reasoned by missing headers in the
sysroot, or by missing 'winsup' folder in gcc's source root folder. Due
to cygwin's tree over tree build mechanism, gcc searches for mingw
targets relative to its root source directory in '../winsup' and
'./winsup' the system headers. You can work-a-round this by generating
the directories 'windsup/mingw/include' within gcc's source tree, and
copy then the runtime-headers of mingw-w64 (/mingw-w64-headers/include'
into it.
