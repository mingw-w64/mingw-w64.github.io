# Known differences to other C-runtime and platform header-sets

## setjmp

### x64 undocumented additional argument

In mingw-w64, setjmp() can take 2 arguments instead of 1. For x86, the
second argument is NULL, for amd64 architecture, it points to the stack
frame before the current frame.

-   see: <a
    href="http://msdn.microsoft.com/en-us/library/xe7acxfb%28VS.80%29.aspx"
    rel="nofollow">http://msdn.microsoft.com/en-us/library/xe7acxfb%28VS.80%29.aspx</a>
