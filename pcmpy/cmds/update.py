import logging
logger = logging.getLogger('pcm')

from pcm.cmds.base import BaseCmd
from pcm.cmds.sync import SyncFirst


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


class UpdateCmd(SyncFirst):
    pacman_args = ('-Su',)
# UpdateCmd
