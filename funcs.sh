pcm_search()
{
    pcm_sync_expire
    pacman -Ss $@    
} #pcm_search

pcm_provides()
{
    pcm_sync_expire
    pkgfile -gsv $@
}

pcm_update()
{
    pcm_sync_expire
    pacman -Su $@ 
} #pcm_update

pcm_sync()
{
    pacman -Sy $@
} #pcm_sync

pcm_sync_expire()
{
    now=$(date +%s)

    if [[ -z $PCM_SYNC_EXPIRE ]]; then
        echo "No expire time set"
        echo $now > "$PCM_LAST_SYNC"
        echo $(pcm_sync $@)
        exit
    fi

    if [[ $PCM_SYNC_EXPIRE -eq 0 ]]; then
        echo "expire is 0, always sync"
        echo $now > "$PCM_LAST_SYNC"
        echo $(pcm_sync $@)
        exit
    fi

    if [[ ! -f "$PCM_LAST_SYNC" ]]; then
        echo "No last sync found, syncing."
        echo $now > "$PCM_LAST_SYNC"
        echo $(pcm_sync $@)
        exit
    fi

    # aged_date=$(date --date="@$(cat $PCM_LAST_SYNC)")
    aged_date=$(cat $PCM_LAST_SYNC)
    delta=$(echo "($now - $aged_date) / 60" | bc)

    last_sync=$(date -d "-$PCM_SYNC_EXPIRE min")

    echo "now $now"
    echo "aged_date $aged_date"
    echo "delta $delta"
    echo "max age $PCM_SYNC_EXPIRE"
    if [[ "$delta" -gt "$PCM_SYNC_EXPIRE" ]]; then
        echo "Last sync was at $(date --date="@$($aged_date)"), re-syncing..."
        echo $now > "$PCM_LAST_SYNC"
        echo $(pcm_sync $@)
        exit
    fi
    
    next_sync=$(date -d "+$(echo $PCM_SYNC_EXPIRE - $delta | bc) min")
    echo "Last sync was at $(date --date="@$aged_date"), not syncing until
    $next_sync"
} #pcm_sync_expire

pcm_install()
{
    echo "pcm_install $@"

    pcm_sync_expire
    pacman -Su $@ 
} #pcm_install
