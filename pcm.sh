#!/bin/bash

BASE_PMAN='pacman'
# if [[ -x '/bin/powerpill' ]]; then
#     BASE_PMAN='/bin/powerpill'
# fi

PMAN="sudo -E $BASE_PMAN"

THIS_DIR="$( cd "$(dirname $(readlink -f ${BASH_SOURCE[0]}) )" && pwd)"
source "$THIS_DIR/funcs.sh"


if [[ -z $PCM_SYNC_EXPIRE ]]; then
    export PCM_SYNC_EXPIRE=60
fi

if [[ -z $PCM_LAST_SYNC ]]; then
    export PCM_LAST_SYNC='/tmp/pcm_last_sync'
fi

if [[ $# -lt 1 ]]; then
    echo "No command given"
    # Kind of nasty ;)
    pacman --help | sed -e 's/pacman/pcm/g'
    echo "pcm wrapper functions:"
    typeset -F | grep -e 'pcm_' | awk '{print $3}' | sed -e 's/^pcm_//g'
    exit 1
fi

naked_cmd="$1"
cmd="pcm_$1"
shift

res=$(type $cmd 2>&1)
c_exists=$?
if [[ "$c_exists" == "1" ]]; then
    $PMAN $naked_cmd $@
    exit
fi

$cmd $@

# vim:set ft=sh:
