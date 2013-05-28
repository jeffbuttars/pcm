#!/bin/bash

repo='git@jeffbuttars.com:users/jeff/pcm'
clone_update  $repo

mkdir $HOME/bin
ln -nsf $HOME/pkgs/pcm/pcm/pcm $HOME/bin/pcm
