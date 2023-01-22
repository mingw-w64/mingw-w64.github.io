# git-sign

## Signing Your Commits

Using GnuPG to sign your commits allow for better traceability, it makes
sure that you actually did commit the change.

### Generating a keypair

To generate a key pair, use:

    gpg --gen-key # follow the on-screen instructions, enter your email address used by the git configuration and password etc

### Signing

To sign, use:

    git commit -S        # sign commit, note upper case
    git tag -s "tag name # sign a tag, note lower case