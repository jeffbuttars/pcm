pcm_search()
{
    pacman -Ss $@    
} #pcm_search

pcm_provides()
{
    pkgfile -gsv $@
}

pcm_update()
{
    pacman -Su $@ 
} #pcm_update

pcm_sync()
{
    pacman -Sy
} #pcm_sync

pcm_install()
{
    pacman -Su $@ 
} #pcm_install
