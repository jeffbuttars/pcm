import logging
logger = logging.getLogger('pcm')

from upkg.cmds.base import BaseCmd


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
    #build()

    def install_pkgs(self, pkgs):
        """todo: Docstring for install_pkgs
        
        :param pkgs: arg description
        :type pkgs: type description
        :return:
        :rtype:
        """
    
        pass
    # install_pkgs()

    def exec(self, args):
        """todo: Docstring for exec

        :param args: arg description
        :type args: type description
        :return:
        :rtype:
        """

        logger.debug("pkgs %s", args.pkgs)
        location = args.location and os.path.abspath(args.pkgs)
        self.install_pkgs(pkgs)
    #exec()
# Cmd
