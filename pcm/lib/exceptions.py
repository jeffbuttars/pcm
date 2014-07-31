class NoPacmanFound(Exception):
    msg = ("The 'pacman' command was not found. Make sure it is installed and "
           "in your in PATH")
    def __init__(self, *args, **kwargs):
        msg = args.pop(0, msg)
        args = [msg] + args
        super(NoPacmanFound, self).__init__(*args, **kwargs)
    # __init__()
#InvalidRepo
