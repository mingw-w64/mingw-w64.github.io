# git-tag

## Tagging

Git tagging is similar in concept to SVN, in which a particular revision
is pegged with a name. To tag, use:

    git tag -a "tag name" [ optional commit ID or object ] # If commit object is unspecified, it will use the current commit
    git push origin "tag name"                             # Push the tag upstream

You are also encouraged to [sign your tag](./git-sign.md).

## Local "lightweight" Tagging

Git allows "lightweight" tags, where the tag is simply a reference to
the actual commit rather than a full new commit with commit author and
date. **Caution** should be used when opting for lightweight tags, since
the tag can be altered even after it is pushed, destroying the original.
It is however fine to use a lightweight tag if you do not plan to push
it to a public repository. To use a lightweight tag, simply omit the -a
argument.
