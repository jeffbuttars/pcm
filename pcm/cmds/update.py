import logging
logger = logging.getLogger('pcm')

from pcm.cmds.base import BaseCmd
from pcm.lib.cmd import PacmanCmd


class Cmd(BaseCmd):
    """Docstring for Cmd """

    name = 'update'
    help_text = ("update pkgname [pkgnames...]")
    aliases = ('up',)

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'pkgs',
            type=str,
            default=None,
            nargs="*",
            help=(""),
        )

        return super(Cmd, self).build()
    # build()

    def exec(self, args):
        """todo: Docstring for exec

        :param args: arg description
        :type args: type description
        :return:
        :rtype:
        """

        logger.debug("pkgs %s", args.pkgs)
        update = UpdateCmd(*args.pkgs)
        update.execute()
    # exec()
# Cmd


class UpdateCmd(PacmanCmd):
    pacman_args = ('-Su',)

    def __init__(self, *pkgs):
        """todo: to be defined

        :param *pkgs: arg description
        :type *pkgs: type description
        """
        super(UpdateCmd, self).__init__(*pkgs)
    # __init__()
# UpdateCmd
