class NoPacmanFound(Exception):
    msg = ("The 'pacman' command was not found. Make sure it is installed and "
           "in your in PATH")
    def __init__(self):
        super(NoPacmanFound, self).__init__(self.msg)
    # __init__()
#InvalidRepo
