# Setup an OSX Buildbot Slave

## Setup an OSX/Darwin Buildbot Slave

Setting up a mingw-w64 OSX / darwin unix buildbot slave requires the
following.

-   Internet connection
-   at least 800mb of ram just for OSX and buildbot, if you have other
    applications running as well they will need to be added to this
    figure.
-   An intel based mac running OSX (Instructions tested with Snow
    Leopard on a 64bit intel mac)

### Install XCode

You will need some tools from XCode to create an OSX hosted buildbot.

Download and install XCode from
<a href="http://developer.apple.com/technology/xcode.html"
rel="nofollow">The apple site</a>, You'll only need "Xcode for Mac-only
Development"

### Install buildbot

Procedure for installing buildbot in OSX Snow Leopard  
This is a simple task if you have OSX Snow Leopard, You may need to
install macports or a gentoo prefix if it doesn't work for you and you
don't have Snow Leopard.

Open a terminal, press Command+Space, Type in "Terminal", press enter.

Install twisted and buildbot: Run these commands in the terminal.

    sudo easy_install twisted
    sudo easy_install buildbot-slave

### Creating the buildbot slave

Now create the buildbot slave, you will need to contact mook on irc to
get the host and port and provide a username and password. [IRC
Details](http://mingw-w64.sourceforge.net/)  
Choose a destination directory for the buildbot, This should have
several gigs of free space and preferably on a case sensitive file
system.  
This example assumes buildbot will be placed in
/Users/&lt;Username&gt;/buildbots/mingw-w64/i686-apple-darwin10  
To get the username, type "cd && pwd" in the terminal, Replace the
&lt;xxx&gt; placeholders with your details

    BUILDBOT_DIR=/Users/<Username>/buildbots/mingw-w64/i686-apple-darwin10
    mkdir -p ${BUILDBOT_DIR} && cd ${BUILDBOT_DIR}
    buildslave create-slave ${BUILDBOT_DIR} <buildbot_host>:<buildbot_port> <username> <password>

You can put any values in for the placeholders and then edit the
**buildbot.tac** file afterwards.  
Now is a good time to edit the buildbot information, This is in
BUILDBOT\_DIR/info, Edit these file to your liking. NOTE : They will be
publicly viewable.

Start buildobt

    buildslave start ${BUILDBOT_DIR}

### Configure Buildbot Autostart

You will most likely want to configure buildbot to start automatically
when OSX boots, These instructions will configure this and start
buildbot

Run these commands in the terminal

    crontab -e

this will take you into VI, In vi, type the following

    [press O to insert a line above the current line and begin insert mode]
    [type in the following line]
    @reboot /usr/local/bin/buildslave start /Users/<Username>/buildbots/mingw-w64/i686-apple-darwin10
    [press escape][type :wq][press enter]

Reboot and ensure your buildbot is connected by navigating to the
darwin-x86-x86 builder at the [Buildbot Master
Details](./buildbot-master-details.md) page.
