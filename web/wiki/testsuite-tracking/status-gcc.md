# testsuite status - gcc

## Summary

Number of expected passes 49008  
Number of unexpected failures 106  
Number of unexpected successes 2  
Number of expected failures 166  
Number of unresolved testcases 77  
Number of untested testcases 35  
Number of unsupported tests 579

------------------------------------------------------------------------

## Failures

FAIL: gcc.c-torture/execute/20070919-1.c execution, -O2  
FAIL: gcc.c-torture/execute/20070919-1.c execution, -O3
-fomit-frame-pointer  
FAIL: gcc.c-torture/execute/20070919-1.c execution, -O3 -g  
FAIL: gcc.c-torture/execute/991014-1.c compilation, -O0  
FAIL: gcc.c-torture/execute/991014-1.c compilation, -O1  
FAIL: gcc.c-torture/execute/991014-1.c compilation, -O2  
FAIL: gcc.c-torture/execute/991014-1.c compilation, -O3
-fomit-frame-pointer  
FAIL: gcc.c-torture/execute/991014-1.c compilation, -O3 -g  
FAIL: gcc.c-torture/execute/991014-1.c compilation, -Os  
FAIL: gcc.c-torture/execute/conversion.c execution, -O0  
FAIL: gcc.c-torture/execute/conversion.c execution, -O1  
FAIL: gcc.c-torture/execute/pr20527-1.c execution, -O3
-fomit-frame-pointer -funroll-loops  
FAIL: gcc.dg/alias-7.c execution test  
FAIL: gcc.dg/c90-const-expr-2.c (test for excess errors)  
FAIL: gcc.dg/c99-const-expr-2.c (test for excess errors)  
FAIL: gcc.dg/large-size-array-2.c (test for errors, line 6)  
FAIL: gcc.dg/large-size-array-4.c (test for errors, line 6)  
FAIL: gcc.dg/pr32370.c (internal compiler error)  
FAIL: gcc.dg/pr32370.c (test for errors, line 16)  
FAIL: gcc.dg/pr32370.c (test for excess errors)  
FAIL: gcc.dg/sync-2.c (test for excess errors)  
FAIL: gcc.dg/utf-cvt.c (test for excess errors)  
FAIL: gcc.dg/utf16-4.c (test for warnings, line 18)  
FAIL: gcc.dg/utf16-4.c (test for excess errors)  
FAIL: gcc.dg/utf32-4.c (test for excess errors)  
FAIL: gcc.dg/matrix/transpose-1.c execution: file transpose-1.gcda does
not exist, -fprofile-generate -O3  
FAIL: gcc.dg/matrix/transpose-2.c execution: file transpose-2.gcda does
not exist, -fprofile-generate -O3  
FAIL: gcc.dg/matrix/transpose-3.c execution: file transpose-3.gcda does
not exist, -fprofile-generate -O3  
FAIL: gcc.dg/matrix/transpose-4.c execution: file transpose-4.gcda does
not exist, -fprofile-generate -O3  
FAIL: gcc.dg/matrix/transpose-5.c execution: file transpose-5.gcda does
not exist, -fprofile-generate -O3  
FAIL: gcc.dg/matrix/transpose-6.c execution: file transpose-6.gcda does
not exist, -fprofile-generate -O3  
FAIL: gcc.dg/struct/w\_prof\_global\_array.c execution: file
w\_prof\_global\_array.gcda does not exist, -O3 -fwhole-program -combine
-fipa-type-escape -fprofile-generate  
FAIL: gcc.dg/struct/w\_prof\_global\_var.c execution: file
w\_prof\_global\_var.gcda does not exist, -O3 -fwhole-program -combine
-fipa-type-escape -fprofile-generate  
FAIL: gcc.dg/struct/w\_prof\_local\_array.c execution: file
w\_prof\_local\_array.gcda does not exist, -O3 -fwhole-program -combine
-fipa-type-escape -fprofile-generate  
FAIL: gcc.dg/struct/w\_prof\_local\_var.c execution: file
w\_prof\_local\_var.gcda does not exist, -O3 -fwhole-program -combine
-fipa-type-escape -fprofile-generate  
FAIL: gcc.dg/struct/w\_prof\_single\_str\_global.c execution: file
w\_prof\_single\_str\_global.gcda does not exist, -O3 -fwhole-program
-combine -fipa-type-escape -fprofile-generate  
FAIL: gcc.dg/struct/w\_prof\_two\_strs.c execution: file
w\_prof\_two\_strs.gcda does not exist, -O3 -fwhole-program -combine
-fipa-type-escape -fprofile-generate  
FAIL: gcc.dg/struct/w\_ratio\_cold\_str.c execution: file
w\_ratio\_cold\_str.gcda does not exist, -O3 -fwhole-program -combine
-fipa-type-escape -fprofile-generate  
FAIL: gcc.dg/tls/opt-11.c (test for excess errors)  
FAIL: gcc.dg/tls/section-2.c (test for errors, line 7)  
FAIL: gcc.dg/torture/fp-int-convert-float80-timode.c -O0 execution
test  
FAIL: gcc.dg/torture/fp-int-convert-float80-timode.c -O1 execution
test  
FAIL: gcc.dg/torture/fp-int-convert-float80-timode.c -O2 execution
test  
FAIL: gcc.dg/torture/fp-int-convert-float80-timode.c -O3
-fomit-frame-pointer execution test  
FAIL: gcc.dg/torture/fp-int-convert-float80-timode.c -O3 -g execution
test  
FAIL: gcc.dg/torture/fp-int-convert-float80-timode.c -Os execution
test  
FAIL: gcc.dg/torture/fp-int-convert-float80.c -O0 execution test  
FAIL: gcc.dg/torture/fp-int-convert-float80.c -O1 execution test  
FAIL: gcc.dg/torture/fp-int-convert-float80.c -O2 execution test  
FAIL: gcc.dg/torture/fp-int-convert-float80.c -O3 -fomit-frame-pointer
execution test  
FAIL: gcc.dg/torture/fp-int-convert-float80.c -O3 -g execution test  
FAIL: gcc.dg/torture/fp-int-convert-float80.c -Os execution test  
FAIL: gcc.dg/torture/fp-int-convert-long-double.c -O0 execution test  
FAIL: gcc.dg/torture/fp-int-convert-long-double.c -O1 execution test  
FAIL: gcc.dg/torture/fp-int-convert-long-double.c -O2 execution test  
FAIL: gcc.dg/torture/fp-int-convert-long-double.c -O3
-fomit-frame-pointer execution test  
FAIL: gcc.dg/torture/fp-int-convert-long-double.c -O3 -g execution
test  
FAIL: gcc.dg/torture/fp-int-convert-long-double.c -Os execution test  
FAIL: gcc.dg/torture/fp-int-convert-timode.c -O0 execution test  
FAIL: gcc.dg/torture/fp-int-convert-timode.c -O1 execution test  
FAIL: gcc.dg/torture/fp-int-convert-timode.c -O2 execution test  
FAIL: gcc.dg/torture/fp-int-convert-timode.c -O3 -fomit-frame-pointer
execution test  
FAIL: gcc.dg/torture/fp-int-convert-timode.c -O3 -g execution test  
FAIL: gcc.dg/torture/fp-int-convert-timode.c -Os execution test  
FAIL: gcc.dg/tree-prof/bb-reorg.c execution: file bb-reorg.gcda does not
exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/indir-call-prof.c execution: file
indir-call-prof.gcda does not exist, -fprofile-generate
-D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/inliner-1.c execution: file inliner-1.gcda does
not exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/pr34999.c execution: file pr34999.gcda does not
exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/stringop-1.c execution: file stringop-1.gcda does
not exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/stringop-2.c execution: file stringop-2.gcda does
not exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/tracer-1.c execution: file tracer-1.gcda does not
exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/update-cunroll-2.c execution: file
update-cunroll-2.gcda does not exist, -fprofile-generate
-D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/update-loopch.c execution: file
update-loopch.gcda does not exist, -fprofile-generate
-D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/update-tailcall.c execution: file
update-tailcall.gcda does not exist, -fprofile-generate
-D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/val-prof-1.c execution: file val-prof-1.gcda does
not exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/val-prof-2.c execution: file val-prof-2.gcda does
not exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/val-prof-3.c execution: file val-prof-3.gcda does
not exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/val-prof-4.c execution: file val-prof-4.gcda does
not exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/val-prof-5.c execution: file val-prof-5.gcda does
not exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/val-prof-6.c execution: file val-prof-6.gcda does
not exist, -fprofile-generate -D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-prof/wcoverage-mismatch.c execution: file
wcoverage-mismatch.gcda does not exist, -fprofile-generate
-D\_PROFILE\_GENERATE  
FAIL: gcc.dg/tree-ssa/loop-1.c scan-assembler-times foo 5  
FAIL: gcc.dg/tree-ssa/loop-3.c scan-tree-dump-times optimized "step:"
1  
FAIL: gcc.dg/tree-ssa/loop-33.c scan-tree-dump-times lim "Executing
store motion of" 4  
FAIL: gcc.dg/tree-ssa/loop-35.c scan-tree-dump-times lim "Executing
store motion of" 8  
FAIL: gcc.dg/tree-ssa/pr27781.c scan-tree-dump optimized "func
\\(\\);"  
FAIL: gcc.dg/tree-ssa/pr33920.c (test for excess errors)  
FAIL: gcc.dg/tree-ssa/ssa-store-ccp-2.c scan-tree-dump-times optimized
"conststaticvariable" 1  
FAIL: gcc.dg/tree-ssa/ssa-store-ccp-3.c scan-tree-dump-times optimized
"conststaticvariable" 1  
FAIL: gcc.dg/tree-ssa/ssa-store-ccp-4.c scan-tree-dump-times optimized
"conststaticvariable" 1  
FAIL: gcc.dg/vect/pr25413.c scan-tree-dump-times vect "vectorized 1
loops" 0  
FAIL: gcc.dg/vect/pr25413.c scan-tree-dump-times vect "vector alignment
may not be reachable" 1  
FAIL: gcc.dg/vect/pr25413.c scan-tree-dump-times vect "not vectorized:
unsupported unaligned store" 1  
FAIL: gcc.dg/vect/pr33833.c (test for excess errors)  
FAIL: gcc.dg/vect/pr33846.c (test for excess errors)  
FAIL: gcc.dg/vect/vect-77-alignchecks.c scan-tree-dump-times vect
"Alignment of access forced using peeling" 1  
FAIL: gcc.dg/vect/vect-78-alignchecks.c scan-tree-dump-times vect
"Alignment of access forced using peeling" 1  
FAIL: gcc.dg/vect/O1-pr33854.c (test for excess errors)  
FAIL: gcc.misc-tests/bprob-1.c execution: file bprob-1.gcda does not
exist, -fprofile-arcs  
FAIL: gcc.misc-tests/bprob-2.c execution: file bprob-2.gcda does not
exist, -fprofile-arcs  
FAIL: gcc.target/i386/pr23943.c (test for excess errors)  
FAIL: gcc.target/i386/pr27971.c scan-assembler-not shr<a
href="../%02klzzwxh%3A0008%03%02klzzwxh%3A0012%03%02klzzwxh%3A0013%03"
class="alink notfound"><code>^</code>\\n</a>*2  
FAIL: gcc.target/i386/pr27971.c scan-assembler and<a
href="../%02klzzwxh%3A0009%03%02klzzwxh%3A0014%03%02klzzwxh%3A0015%03"
class="alink notfound"><code>^</code>\\n</a>*12  
FAIL: gcc.target/i386/sse-9.c (test for excess errors)  
FAIL: gcc.target/i386/sse5-haddX.c (test for excess errors)  
FAIL: gcc.target/i386/sse5-hsubX.c (test for excess errors)