# History

## A Brief History

Mingw-w64 was started in order to port an ObjectiveC application to
64bit Windows in 2005. The only compiler targeting Windows that
supported ObjectiveC was the
<a href="http://gcc.gnu.org" rel="nofollow">GCC</a> compiler from MinGW.

<a href="http://www.onevision.com" rel="nofollow">OneVision</a> began
<a href="http://en.wikipedia.org/wiki/Clean_room_design"
rel="nofollow">clean room</a> of the 64bit Windows API. The work was
presented to the MinGW developers at mingw.org after the initial port of
the GNU toolchain and the headers/startup sources were completed by
OneVision?. It was rejected on the suspicion of using non-public
proprietary sources of information (
<a href="http://article.gmane.org/gmane.comp.gnu.mingw.devel/3390"
rel="nofollow">additional infos</a>).

The mingw-w64 project was then created as a fork of the original MinGW
project to prevent the work from being lost. It was registered on
sourceforge on August 2007, with the public code repository up by
October 2007. In 2008, OneVision? donated the mingw-w64 code to Kai
Tietz on the condition that it remains Open Source. Kai currently works
on maintaining the GNU toolchain to support both 32bit and 64bit
Windows.

## Policy

One of the founding policies of the mingw-w64 project is that any code
change to external tools (GCC, binutils, gdb, ...) must be merged back
upstream in order to prevent bit rot often associated with private
working trees. This means that the vanilla FSF-released GNU toolchains
are often built and used directly without any extra patch.

Mingw-w64 accepts clean room reverse-engineered code, such as those from
<a href="http://reactos.org/" rel="nofollow">ReactOS</a> and
<a href="http://www.winehq.org/" rel="nofollow">Wine</a>, in contrast to
the original mingw.org project where all contributions must be sourced
from the
<a href="http://msdn.microsoft.com/en-us/library/" rel="nofollow">MSDN
Library</a>. The difference in policy is a major dividing issue between
the two projects and a source of contention as of writing.
