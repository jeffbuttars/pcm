
PMAN='sudo -E pacman'

pcm_search()
{
    pcm_sync_expire
    $PMAN -Ss $@    
    res=$?
    if [[ "$res" == "1" ]]; then
        echo "Trying yaourt"
        yaourt $@
    fi
} #pcm_search

pcm_flist()
{
    $PMAN -Ql $@
}

pcm_provides()
{
    pcm_sync_expire
    res=$(pkgfile -gsv $@)
    if [[ "$res" == "" ]]; then
        echo "no match found for '$@'"
        exit 1
    fi

    echo "$res"
}

pcm_update()
{
    pcm_sync_expire
    $PMAN -Su $@

    if [ -x /usr/bin/yaourt ]; then
        yaourt --noconfirm -Sua
    fi
} #pcm_update

pcm_up()
{
    pcm_update $@
} #pcm_up

pcm_sync()
{
    echo "pcm_sync $@"
    $PMAN -Sy $@
    sudo -E pkgfile --update
} #pcm_sync

pcm_makecache()
{
    pcm_sync $@
} #pcm_makecache

pcm_sync_expire()
{
    now=$(date +%s)

    if [[ -z $PCM_SYNC_EXPIRE ]]; then
        echo "No expire time set"
        echo $now > "$PCM_LAST_SYNC"
        echo $(pcm_sync $@)
        PCM_SYNC_EXPIRE=1440
    fi

    if [[ $PCM_SYNC_EXPIRE -eq 0 ]]; then
        echo "expire is 0, always sync"
        echo $now > "$PCM_LAST_SYNC"
        echo $(pcm_sync $@)
    fi

    if [[ ! -f "$PCM_LAST_SYNC" ]]; then
        echo "No last sync found, syncing."
        echo $now > "$PCM_LAST_SYNC"
        pcm_sync $@
    fi

    # aged_date=$(date --date="@$(cat $PCM_LAST_SYNC)")
    aged_date=$(cat $PCM_LAST_SYNC)
    echo "aged_date: $aged_date"
    delta=$(echo "($now - $aged_date) / 60" | bc)
    echo "delta: $delta"

    last_sync=$(date -d "-$PCM_SYNC_EXPIRE min")
    echo "last_sync: $last_sync"

    echo "now $now"
    echo "aged_date $aged_date"
    echo "delta $delta"
    echo "max age $PCM_SYNC_EXPIRE"
    if [[ "$delta" -gt "$PCM_SYNC_EXPIRE" ]]; then
        echo "Last sync was at $(date --date="@${aged_date}"), re-syncing..."
        echo $now > "$PCM_LAST_SYNC"
        echo $(pcm_sync $@)
    fi
    
    next_sync=$(date -d "+$(echo $PCM_SYNC_EXPIRE - $delta | bc) min")
    # echo "Last sync was at $(date --date="@$aged_date"), not syncing until $next_sync"
} #pcm_sync_expire

pcm_install()
{
    # echo "pcm_install $@"

    pcm_sync_expire
    $PMAN -S $@ 
    res=$?
    if [[ "$res" == "1" ]]; then
        echo "Trying yaourt"
        yaourt $@
    fi
} #pcm_install

pcm_in()
{
    pcm_install $@
} #pcm_in

pcm_remove()
{
    $PMAN --remove $@
} #pcm_remove

pcm_uninstall()
{
    pcm_remove $@
} #pcm_uninstall

pcm_info()
{
    pcm_sync_expire
    $PMAN  -Qi $@
} #pcm_info
