# Internal heap management functions

There are different ways to implement internal memory management. The
first and most obvious way is via the Win32 Heap&lt;...&gt; API
(HeapAlloc?, HeapCreate?, HeapDestroy?, HeapReAlloc?, HeapFree?,
HeapSize?, HeapValidate?, HeapCompact?, GetProcessHeap?, and
GetProcessHeaps? are the Win32 API functions). The second implementation
way is via the Virtual&lt;...&gt; API of win32 (VirtualFree?(Ex),
VirtualProtect?(Ex), VirtualQuery?(Ex), VirtualAlloc?(Ex) functions).

For optimizing heap memory usage thunking of small memory allocation
within one heap allocation block is used.

There are at least three different windows heap allocation schema. There
is the system heap, VC5 heap, and VC6 heap. Beside the system heap, all
others are aligned to a 16-byte alignement. Even for zero byte
allocations, at least one byte gets allocated for Windows heap.

The small thunks (sbh) are allocated for 32-bit memory block size gets
aligned to 4 bytes, for 64-bit on a 8 bytes.