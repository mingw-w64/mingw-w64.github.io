# Create a buildbot slave

## Creating a buildbot slave

The mingw-w64 project relies on buildbots to create the weekly and
nightly releases of the mingw-w64 toolchains. This also serves as a
quality assurance measure to check if the toolchains will compile
successfully with the latest code.

Many buildbots are needed in order to create all the variaties of
toolchains. The targets are i686-w64-mingw32 and x86\_64-w64-mingw32.
The hosts are cygwin, mingw-w64 32bit, mingw-w64, darwin unix (OSX),
linux 32bit and linux 64bit. That equates to 12 independent builds of
binutils, gcc, mingw-w64 and supporting libs every night.

### Buildbot Slave Howtos

-   [howto : Setup an OSX Buildbot Slave](./setup-an-osx-buildbot.md)
-   [howto : Setup a Cygwin Buildbot Slave](./setup-a-cygwin-buildbot.md)
-   [howto : Setup a MSYS Buildbot Slave](./setup-a-msys-buildbot.md)
