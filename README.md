# PCM - A yum like wrapper for pacman

A simple shell command wrapper to create a yum like command, `pcm`, for those
used to using yum and moving to arch. Or for those who would prefer a less
cryptic command syntax for common pacman and pkgfile commands.

## Install

I don't have a formal installer. I recommend cloning the repo somewhere you can
keep it around. I use a directory called `pkgs` in my $HOME. Then link the `pcm`
command into your `~/bin/`. For example:

    > cd
    > mkdir -p pkgs
    > cd pkgs
    > git clone https://github.com/jeffbuttars/pcm.git pcm
    > mkdir -p ~/bin
    > ln -s $HOME/pkgs/pcm/pcm $HOME/bin/

Then, make sure that `$HOME/bin` is in your path. A line like the following in
your `$HOME/.bashrc` should do it:

    export PATH="$HOME/bin:$PATH"


## Commands

The command syntax is simply:

    > pcm <command> <args>

### install

Install a package or list of packages.

    > pcm install pkg1 pkg2 ...


### remove, uninstall

remove/uninstall a package or list of packages

    > pcm remove pkg1 pkg2 ...
    > pcm uninstall pkg1 pkg2 ...


### provides

Find packages that contain a file matching a regex.

    > pcm provides '*/headerfile.c'


### update

Update all installed packages or update specified packages..  

Update the system:

    > pcm update

Update kde:

    > pcm update kde

### sync, makecache

Update the package and pkginfo local databases

    > pcm sync
    > pcm makecache


### info

Get information about a package or packge group

    > pcm info pkgname
    > pcm info pkggroup
