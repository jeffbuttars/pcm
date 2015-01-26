import logging
logger = logging.getLogger('pcm')

from pcm.cmds.base import BaseCmd
from pcm.lib.cmd import Cmd


class Cmd(BaseCmd):
    """Docstring for Cmd """

    name = 'provides'
    help_text = ("provides <path_expresssion>")

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'path',
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
        provides = ProvidesCmd(args.path)
        provides.execute()
    # exec()
# Cmd


class ProvidesCmd(Cmd):
    command = 'pkgfile -gsv'
# InstallCmd
