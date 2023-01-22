# git

If instructions are confusing or require additional clarification,
please bring it on on the
<a href="irc://irc.oftc.net/%23mingw-w64" rel="nofollow">irc channel</a>
or the [Mailing List](../mailing-list.md).

## git Basic Operations

The act of downloading from a git repo is called "pulling", and
affecting the contents of a remote repository is called "pushing". In
contrast to SVN, where a remote repository is downloaded as a local
working copy, git "clones" the entire remote repository and then makes a
working directory, so any commits, merges, branching are ALWAYS towards
the local cloned git repository until it is pushed. Typically, you can
review all your changes after having done them on the local repository
and BEFORE pushing to the remote repository.

This section of the guide assumes you want to make a trivial change and
have not checked out any code. Go to the "Working on your changes" part
if you have already cloned the mingw-w64 repository.

### Before Starting

You should always set your git username and email address before using
git. It is used to identify and credit commits by users. Do this by
issuing:

    git config user.name "firstname lastname"
    git config user.email "user@mail.com"

### git cloning

This will replicate the remote repository to the current working
directory and produce a working copy as with SVN. The only notable
difference is that there is a .git directory instead of .svn. Th clone
command is:

    git clone <url> <local dir to put the clone in>

### Updating

If you have no changes to your local working copy, just use "git pull"
to update.

### Working on your changes

It is recommended that you start a new branch to do your changes, so it
does not get disrupted when updating from the remote repository. Under
SVN, the main branch is usually called "trunk", and "master" under git.
Use the following commands to branch (assuming branching from master):

    git branch --track MyFeatureBranch origin/master # create our MyFeatyureBranch, it will be based off origin/master
    git checkout MyFeatyureBranch                    # switch to our new branch

"origin/master" refers to the "master" branch on the "origin" remote,
where "origin" is the git repository that the local copy was cloned
from.

#### Viewing your Changes

Use the following to view your changes

    git diff

#### Committing Your Changes

Once you are done with your changes and happy with the result, you
should use "git add" to stage the files that are relevant to the new
commit. This includes BOTH new AND modified existing files.

    git status             # List all modified and new files
    git add file1 file2... # add files to staging area
    git diff --cached      # See difference between base version and staged
    git commit             # Be sure to set the EDITOR environment variable to your favored text editor, eg EDITOR=nano

You are encouraged to use GnuPG to [sign your
commits](./git-sign.md) for better authentication and
traceability. Commit messages should be in the form of:

    Short 1-line description
    <blank line>
    Long multi-line description of the change
    with any justification reasons

After committing your change you can compare your current branch to the
upstream with:

    git diff origin/master..HEAD # in case master is upstream

Note that all commits are local and not yet visible to others over the
internet. You can run through this step multiple times to break up large
works into multiple logical commits to ease review, an update to the
remote repository is not required for you to be able to commit locally
again.

#### Making Your Changes Visible

Before going any further, you should make sure to update your local
repository:

                             # There are multiple ways to accomplish the same actions, this is simply one of them
    git fetch origin         # Pull updates from remote repository, it will not overwrite your changes at all
    git rebase origin/master # Rebase your commits, so it looks it like it was committed after the latest remote changes
                             # If there are any conflicts, follow the on-screen instructions, mark files are resolved via git add

    git diff origin/master..myfeaturebanch         # review changes for the last time
    git format-patch origin/master..myfeaturebanch # produce patches for review by email submission if you have no git push access or uncomfortable with pushing

                                                   # continue with push operation if you have push access, you should still review your changes with the
                                                   # mingw-w64 developers first
    git push origin myfeaturebanch:master          # push your local myfeaturebanch over the remote master

#### Cleaning Up

After your (or someone else with push access) has pushed your changes,
you can delete your private branch or keep it at your discretion. To
delete:

    git checkout master          # switch back to the original
    git pull                     # optional, bring it up to date since we last checked it out
    git branch -d myfeaturebanch # delete your merged branch.

------------------------------------------------------------------------

## Backporting Specific Changes

See [backporting](./git-backport.md)

## Creating Tags

See [tagging](/git-tag.md)

## Creating Stable Branches

See git stable branch?

## Reverting Changes

See [git revert](./git-revert.md)
