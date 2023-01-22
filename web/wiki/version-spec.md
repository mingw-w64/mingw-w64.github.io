# MinGW-w64 Versioning Specification

## Goals

-   Enhance project maintainability by providing a set of versioning
    rules used for developing, building, and releasing
-   Facilitate better communication between project contributors and
    end-users, both human and machine.

## Format

-   MAJOR "." MINOR
    <a href="../%22-%22%20SUFFIX" class="alink notfound">["-" SUFFIX]</a>
    where optional SUFFIX := "a" | "b" | "pre" |
    "rcX<a href="../Y" class="alink notfound">[Y]</a>"

-   Newer versions are numerically and lexically greater than previous
    versions according to the following example

        1.0-pre < 1.0 < 1.1-a < 1.1-b < 1.1-pre < 1.1-rc1 < 1.1-rc2 < 1.1 < 2.0-a < 2.0

-   "a" indicates "alpha" code quality level

-   "b" indicates "beta" code quality level

-   "pre" indicates "pre-release" code quality level

-   "rcX<a href="../Y" class="alink notfound">[Y]</a>" indicates
    "release candidate" code quality levels and are tagged in the source
    repository

## SVN

### Source Repository Layout

    +- trunk/
    +- experimental/
    +- stable/
        +- v1.x/
        +- v2.x/
    +- tags/
        +- releases/
            +- v1.0/
            +- v1.1-rc1/
            +- v1.1-rc2/
            +- v1.1/
            +- v2.0-rc1/
            +- v2.0/

### Typical Source Repository Workflow

-   Develop alpha (*a*) versions only in experimental branches
-   Develop beta (*b*) versions only in trunk
-   When starting new pre-release code, create a new stable branch
    (stable/vA.x)
-   To make a new release of a stable branch, set the version SUFFIX to
    *rcX*, test, and tag a release (tags/releases/v1.1-rc1). Commit only
    to fix release blockers. Bump the *rcX* version SUFFIX when it makes
    logical sense to do so.
-   When there are no more blockers on a stable branch, tag a final
    release (tags/releases/v1.1). The next stable branch commit
    following the final release should set the version back to *pre*
    with a MAJOR or MINOR version bump. When a stable branch is in final
    release, the only allowed commit is to move it back to *pre*.

## Automated and Personal Build Download Release Naming

**TODO** coordinate with Ruben and integrate with current naming scheme

# Questions

1.  If *a*, *b*, and *pre* releases aren't tagged, how does one quickly
    build that version in order to replicate issues?

> NS: People having issues in those areas are going to say "I have an
> issue with revision ABC"
>
> Jon: If you're going to make downloads for those, you'll want an easy
> way to checkout a working dir to that revision

1.  If only going to tag *rc* and final releases, why not remove *tags*
    dir and hoist *releases* dir in its place?

> NS: We could in the future have other kinds of tags than just
> releases. Maybe a tech preview, maybe a snapshot, maybe something from
> experimental, etc.
