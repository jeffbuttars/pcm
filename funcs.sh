
pcm_search()
{
    pcm_sync_expire
    pacman -Ss $@    
    res=$?
    if [[ "$res" == "1" ]]; then
        echo "Trying yaourt"
        yaourt $@
    fi
} #pcm_search

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
    pacman -Su $@ 
} #pcm_update

pcm_up()
{
    pcm_update $@
} #pcm_up

pcm_sync()
{
    echo "pcm_sync $@"
    pacman -Sy $@
    pkgfile --update
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
    delta=$(echo "($now - $aged_date) / 60" | bc)

    last_sync=$(date -d "-$PCM_SYNC_EXPIRE min")

    # echo "now $now"
    # echo "aged_date $aged_date"
    # echo "delta $delta"
    # echo "max age $PCM_SYNC_EXPIRE"
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
    pacman -S $@ 
} #pcm_install

pcm_in()
{
    pcm_install $@
} #pcm_in

pcm_remove()
{
    pacman --remove $@
} #pcm_remove

pcm_uninstall()
{
    pcm_remove $@
} #pcm_uninstall

pcm_info()
{
    pcm_sync_expire
    pacman  -Qi $@
} #pcm_info
