# Setup a MSYS Buildbot Slave

## Setup a MSYS Buildbot Slave

These instructions were tested with a Vista 64bit machine. Note that the
installation steps require elevation in order to write into the root of
the disk. All versions listed are as used; newer versions may be
available, and are likely to work as well.

### Install MinGW

The MinGW toolchain can either be the mingw-w64 version, or the
mingw.org version:

#### Dogfooding MinGW

Download one of the toolchains from
[SourceForge](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/)
and extract it to `C:\MinGW`. You should end up with a
`C:\MinGW\bin\gcc.exe`.

#### Using mingw.org binaries

Install MinGW (32 bit) following mingw.org
<a href="http://www.mingw.org/wiki/Getting_Started#toc2"
rel="nofollow">instructions</a>; according to their Getting Started
page, manual installation is preferred. Using
<a href="http://www.7-zip.org/" rel="nofollow">7-zip</a>, extract the
following files to C:\\MinGW, using the newer file whenever there is a
conflict:

-   binutils-2.20-1-mingw32-bin.tar.gz
-   gcc-c++-4.4.0-mingw32-bin.tar.gz
-   gcc-c++-4.4.0-mingw32-dll.tar.gz
-   gcc-core-4.4.0-mingw32-bin.tar.gz
-   gcc-core-4.4.0-mingw32-dll.tar.gz
-   gmp-4.2.4-mingw32-dll.tar.gz
-   libiconv-1.13.1-1-mingw32-dll-2.tar.lzma
-   mingwrt-3.17-mingw32-dev.tar.gz
-   mingwrt-3.17-mingw32-dll.tar.gz
-   mpfr-2.4.1-mingw32-dll.tar.gz
-   pthreads-w32-2.8.0-mingw32-dll.tar.gz
-   w32api-3.14-mingw32-dev.tar.gz

### Installing MSYS

Install MSYS (32 bit) following the mingw.org
<a href="http://www.mingw.org/wiki/MSYS#toc0"
rel="nofollow">instructions</a>.

-   MSYS-1.0.11.exe installs into the default directory of
    C:\\msys\\1.0 - tell it about the MinGW install from above.
-   msysDTK-1.0.1.exe installs into the same place.
-   msysCORE-1.0.12-1-msys-1.0.12-bin.tar.lzma update - again, using
    7-zip.

Install extra MSYS updates:

-   bash-3.1.17-2-msys-1.0.11-bin.tar.lzma
-   bison-2.4.1-1-msys-1.0.11-bin.tar.lzma
-   coreutils-5.97-2-msys-1.0.11-bin.tar.lzma
-   crypt-1.1\_1-2-msys-1.0.11-bin.tar.lzma
-   flex-2.5.35-1-msys-1.0.11-bin.tar.lzma
-   libcrypt-1.1\_1-2-msys-1.0.11-dll-0.tar.lzma
-   libregex-0.12-1-msys-1.0.11-dll-0.tar.lzma
-   libregex-1.20090805-1-msys-1.0.11-dll-1.tar.lzma
-   make-3.81-2-msys-1.0.11-bin.tar.lzma
-   perl-5.6.1\_2-1-msys-1.0.11-bin.tar.lzma
-   texinfo-4.13a-1-msys-1.0.11-bin.tar.lzma

### Installing Buildbot

-   Install
    <a href="http://www.python.org/download/" rel="nofollow">Python</a> -
    python-2.6.4.msi (due to Twisted version below)
-   Install [pywin32](https://sourceforge.net/projects/pywin32/files/) -
    pywin32-214.win32-py2.6.exe
-   Install <a href="http://twistedmatrix.com/trac/wiki/Downloads"
    rel="nofollow">Twisted</a> - Twisted-9.0.0.win32-py2.6.exe
-   Download
    [Buildbot](http://sourceforge.net/projects/buildbot/files/buildbot/0.8.2/buildbot-slave-0.8.2.zip/download) -
    buildbot-slave-0.8.2.zip
-   Extract the Buildbot zip and run `python setup.py install`
    (easy\_install appears to be broken)

### Odds and ends

-   Download
    <a href="http://technet.microsoft.com/en-us/sysinternals/bb896768.aspx"
    rel="nofollow">Junction.exe</a> and place it in the path somewhere.
    Run it once to accept the license.
-   Download <a href="ftp://ftp.info-zip.org/pub/infozip/win32/"
    rel="nofollow">zip</a> and place it in the path.
-   Add `C:\Python26` and `C:\Python26\Scripts` to your PATH.
-   Set `MACHTYPE=i686-pc-msys` in the (persisted) environment,
    otherwise <a
    href="http://github.com/djmitche/buildbot/commit/aa64ff3b96139f401da893379be1ee5eb9384d94"
    rel="nofollow">Buildbot</a> gets confused.

### Creating the buildbot slave

Now create the buildbot slave, you will need to contact Mook on irc to
get the host and port and provide a username and password. [IRC
Details](http://mingw-w64.sourceforge.net/)  
Choose a destination directory for the buildbot, This should have
several gigs of free space.  
This example assumes buildbot will be placed in
c:\\buildbots\\mingw-w64\\i686-pc-mingw32  
Replace the &lt;xxx&gt; placeholders with your details

    BUILDBOT_DIR=/c/buildbots/mingw-w64/i686-pc-mingw32
    mkdir -p ${BUILDBOT_DIR} && cd ${BUILDBOT_DIR}
    buildslave create-slave ${BUILDBOT_DIR} <buildbot_host>:<buildbot_port> <username> <password>

You can put any values in for the placeholders and then edit the
**buildbot.tac** file afterwards.  
Now is a good time to edit the buildbot information, This is in
BUILDBOT\_DIR/info, Edit these file to your liking. NOTE : They will be
publicly viewable.

Start Buildbot

    buildslave start ${BUILDBOT_DIR}

### Configure Buildbot Autostart

The current build slaves have a fork of `C:\msys\1.0\msys.bat` set to
automatically launch Buildbot. It is important to do so under MSYS bash
so that the environment is correctly set up. The batch file is then
started on boot via the Task Scheduler.
