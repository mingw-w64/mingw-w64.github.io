# threadc79 internal-error

**Q:**  
Why do i get the following error message in GDB?

    gdb: unknown target exception 0xc0000135 at 0x77f52909

    Program exited with code 0200.
    ../../gdb-cvs/gdb/thread.c:79: internal-error: inferior_thread: Assertion `tp' failed.
    A problem internal to GDB has been detected,

**A:**  
This is most likely because GDB is unable to locate DLLs required to run
your program. To confirm this : Quit GDB and run the program from the
same command window. If the required DLL(s) are unable to be located you
will be prompted with a windows error message. This error message should
tell you which DLL it's unable to locate.

To fix this problem, Find the location of the DLL and add its directory
to the PATH variable.

    set PATH=%PATH%;c:\where\dll\is

Retry running the executable from the command prompt, If it succeeds
then you should now be able to debug the program in GDB.
