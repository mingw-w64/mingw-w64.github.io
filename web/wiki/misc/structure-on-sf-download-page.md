# Structure on SF download page

The structure and the naming on our [download
page](http://sourceforge.net/projects/mingw-w64/files/) is following
pretty ease rules.

The folders of general interest are "mingw-w64", "Toolchains targetting
Win64", "Toolchains targetting Win32", and "Toolchain sources".

In the folder "mingw-w64" you can find in "mingw-w64-snapshot" the
source-tar-ball for releases.

In the folder "Toolchains targetting Win64" you can find pre-build
toolchains for different hosts targeting for 64-bit Windows. In the
sub-folder "Automated Builds" you can find pre-build toolchains created
by our buildbot. Right now we are building two different variants here.
One is the 1.0 branch build and the other is our trunk version. The 1.0
version gets build by using binutils head and gcc 4.6.x branch. You will
find for those pre-build toolchains the version 1.0 in name. The other
is using mingw-w64 trunk, gcc trunk, and binutils head version for
building. For this variant there is no version number in name. The
naming of binary-packages is "mingw-w64-" optional the version number of
mingw-w64 "bin-" host-triplet "\_" data-of-build. In the sub-directory
"Personal Builds" you can find pre-build toolchains provided by
different people targeting for 64-bit Windows. Please read here the
description provided to those packages to see what additional features
were actived for them.

In the folder "Toolchains targetting Win32" you can find pre-build
toolchains for different hosts targeting for 32-bit Windows. In the
sub-folder "Automated Builds" you can find pre-build toolchains created
by our buildbot. Right now we are building two different variants here.
One is the 1.0 branch build and the other is our trunk version. The 1.0
version gets build by using binutils head and gcc 4.6.x branch. You will
find for those pre-build toolchains the version 1.0 in name. The other
is using mingw-w64 trunk, gcc trunk, and binutils head version for
building. For this variant there is no version number in name. The
naming of binary-packages is "mingw-w32-" optional the version number of
mingw-w64 "bin-" host-triplet "\_" data-of-build. In the sub-directory
"Personal Builds" you can find pre-build toolchains provided by
different people targeting for 64-bit Windows. Please read here the
description provided to those packages to see what additional features
were actived for them.

The last folder of interest is the "Toolchain sources". Here you can
find the source-tar-balls used for the various pre-build binary-pages.

Two additional folders need to be mentioned here, too. In the folder
"3rd party development tools" you can find a version for "autotools". In
"External binary packages (Win64 hosted)" you will find variour prebuild
libraries and tools for 64-bit Windows.
