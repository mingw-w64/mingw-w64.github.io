# default_manifest

**Q:**  
What are default manifest files and why do they matter?

**A:**

### Background

Windows Vista and later adds User Account Control capability and ran
programs without administrator privileges by default. Executable names
containing setup, install, patch, update causes UAC prompt popups to the
user, which may not be appropriate.

The manifest file also sets the Windows compatibility level of an
executable since Windows XP. Prior to Windows 8.1, it is fully under
control of the user, later versions of Windows require that the
application manifest declaring the executable compatibility level, or
risk running under the oldest available compatibility layer (Windows
Vista on 8.1).

### Default Manifest

The windows-default-manifest project under Cygwin was created to allow a
common manifest to be used by all toolchains targeting Windows. The
resource file will contain the latest compatibility GUID to disable
Windows compatibility levels and make executable images always run as
the invoked user. As of writing (April 2014), there is some support in
binutils ld to implicitly link the default manifest resource, but the
implementation is being moved to gcc to automatically link it if it was
installed.