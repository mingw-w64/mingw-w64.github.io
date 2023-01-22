# Backporting

First, find the file you wish to backport from, for example, crt/io.h on
master, then look for the interested commit with:

    git log -p mingw-w64-headers/crt/io.h

It should produce something akin to:

    commit b33bcd6aba7a789e6e3ce66114651a92b9bcb170
    Author: ...
    Date:   ...

        Moved srtuct declarations from _mingw.h to crtdefs.h

    diff --git a/mingw-w64-headers/crt/io.h b/mingw-w64-headers/crt/io.h
    index 67ee5ae..b68393a 100644
    --- a/mingw-w64-headers/crt/io.h
    +++ b/mingw-w64-headers/crt/io.h
    @@ -6,7 +6,7 @@
    ...

    commit 8a67ab4541226a80b3ec2047347890d915126de1
    Author: ...
    Date:   ...

        Replace 'w64 mingw-runtime' by 'mingw-w64 runtime'

        Also replace 'This file is a part of' by 'This file is part of' for consistency

    diff --git a/mingw-w64-headers/crt/io.h b/mingw-w64-headers/crt/io.h
    index 16c1e86..67ee5ae 100644
    --- a/mingw-w64-headers/crt/io.h
    +++ b/mingw-w64-headers/crt/io.h
    ...

note the commit IDs, once you have a list of commits to backport, switch
to the branch to backport the changes to with git checkout. Next, use:

    git cherry-pick -x ID1 ID2 ID3...

to pick the patches to apply.

For more complex backporting, you may want to use -n to merge each
changes so you can preview and/or make changes before it is committed.

    git cherry-pick -x -n ID1
    git commit
    git cherry-pick -x -n ID2
    ...
    git cherry-pick -x -n ID3
    ...
