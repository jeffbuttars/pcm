import logging
logger = logging.getLogger('pcm')

from pcm.cmds.base import BaseCmd
from pcm.cmds.sync import SyncFirst


class Cmd(BaseCmd):
    """Docstring for Cmd """

    name = 'install'
    help_text = ("install pkgname [pkgnames...]")
    aliases = ('in',)

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'pkgs',
            type=str,
            default=None,
            nargs="+",
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
        installer = InstallCmd(*args.pkgs)
        installer.execute()
    # exec()
# Cmd


class InstallCmd(SyncFirst):
    pacman_args = ('-S',)
# InstallCmd
