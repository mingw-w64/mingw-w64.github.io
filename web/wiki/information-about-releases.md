# Information about releases of mingw-w64

To understand the way mingw-w64 did in the past for 1.0 branch the
releasing, needs some description. At the beginning we were using
rolling-release mechanism. Which means that we didn't branched/tagged
for new releases. This meant that each snapshot itself was an new
release. This approach has proven to be not usable and accepted by most
of our users. So we created the 1.0 version branch, but still there were
no specific version tags used on this branch. Means the 1.0 branch was
still a rolling release.

As this approach has still shown the same problems to our users as
initial approach, we decided now to use branches for major versions and
tag explicit a version as release. Those tags can be found in our
svn-repository as usual under /tags/ tree.
