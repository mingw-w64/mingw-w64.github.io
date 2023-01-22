# Nokia's Qt

Qt is a popular cross-platform framework and has demonstrated its power
yet again by being easy to fix for a new toolchain.

## How to build

-   Currently, Qt 4.7 from git is the recommended way to go. You will
    need to clone the repository or download a tar.gz from
    <a href="http://qt.gitorious.org/qt/qt/trees/4.7" rel="nofollow">this
    page</a>. You can extract

-   As this is source from git, you will need
    <a href="http://strawberryperl.com/" rel="nofollow">perl</a> for
    some pre-configuration steps. Install perl and restart your cmd
    shell (or add the location of perl.exe to PATH).

-   Set up a cmd environment for mingw-w64:
    [GeneralUsageInstructions](../general-usage-instructions.md)

-   `cd` to where the Qt source is located and run (you can see all
    possible options by doing `configure -h`)

        configure -qt-style-windowsxp -qt-style-windowsvista -phonon

These extra options are required because `configure` is stupid and can't
find the relevant headers required for these features. It should be
fixed upstream and will be included in 4.8.  
\* After configure finishes, run `mingw32-make` and wait a couple of
hours.

The x64 patches were too late for the 4.6 branch, but a mingw-w32
toolchain (builds 32-bit apps) should have no problem with the official
4.6 source (disable WebKit, Script, ActiveQt, these contain mingw.org
specificic code which breaks under mingw-w64/w32, which adheres more
closely to MSVC).