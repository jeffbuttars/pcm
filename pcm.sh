#!/bin/bash

THIS_DIR="$( cd "$(dirname $(readlink -f ${BASH_SOURCE[0]}) )" && pwd)"
source "$THIS_DIR/funcs.sh"


if [[ -z $PCM_SYNC_EXPIRE ]]; then
    export PCM_SYNC_EXPIRE=60
fi

if [[ -z $PCM_LAST_SYNC ]]; then
    export PCM_LAST_SYNC='/tmp/pcm_last_sync'
fi

# echo "$@"

if [[ $# -lt 1 ]]; then
    echo "No command given"
    exit 1
fi

naked_cmd="$1"
cmd="pcm_$1"
shift

# if [[ "$cmd" == "pcm_sync" ]]; then
#     cmd="pcm_sync_expire"
# fi

# echo "$cmd $@"
res=$(type $cmd 2>&1)
c_exists=$?
if [[ "$c_exists" == "1" ]]; then
    pacman $naked_cmd $@
    exit
fi

$cmd $@

# vim:set ft=sh: