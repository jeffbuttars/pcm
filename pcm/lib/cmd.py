import logging
logger = logging.getLogger('pcm')

import sys
import subprocess
# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO

from blessings import Terminal

# from pcm.lib.exceptions import NoPacmanFound


class Cmd(object):
    """Docstring for PkgrExec """

    command = ''

    def __init__(self, *args, command=None):
        """todo: to be defined

        :param pkgr: arg description
        :type pkgr: type description
        :param args: arg description
        :type args: type description
        """
        self.command = command
        self._args = args

        self.term = Terminal()
    # __init__()

    def __repr__(self):
        return "{} {}".format(
            self._command,
            self._args,
        )
    # __repr__()

    def __str__(self):
        return self.__repr__()
    # __str__()

    def _build_writer(self, output, color=None, prefix=""):
        if color:

            def _cwriter(line):
                go = getattr(self.term, color)
                output.write(go(prefix + line))
                output.flush()

            return _cwriter

        def _writer(line):
            output.write(prefix + line)
            output.flush()

        return _writer
    # _build_writer()

    def _sh_stdout(self, *args, **kwargs):
        return self._build_writer(sys.stdout, *args, **kwargs)
    # _sh_stdout()

    def _sh_stderr(self, *args, **kwargs):
        return self._build_writer(sys.stderr, *args, **kwargs)
    # _sh_stderr()

    def pr_pass(self, fmt, *args, **kwargs):
        print(self.term.green(fmt.format(*args, **kwargs)))
    # pr_pass()

    def pr_info(self, fmt, *args, **kwargs):
        print(self.term.blue(fmt.format(*args, **kwargs)))
    # pr_info()

    def pr_fail(self, fmt, *args, **kwargs):
        print(self.term.red(fmt.format(*args, **kwargs)))
    # pr_fail()

    def pr_atten(self, fmt, *args, **kwargs):
        print(self.term.red(fmt.format(*args, **kwargs)))
    # pr_atten()

    @property
    def command(self):
        return self.command
    # cmd()

    def execute(self):
        logger.debug("%s %s", self.command, self._args)
        try:
            subprocess.check_call(
                (self.command,) + self._args,
            )
        except subprocess.CalledProcessError as e:
            sys.exit(e.returncode)
    # execute()
# Cmd


class PacmanCmd(Cmd):
    """Docstring for PkgrCmd """
    pacman_args = ()
    command = 'pacman'

    def __init__(self, *args):
        """todo: to be defined

        :param pkgr: arg description
        :type pkgr: type description
        :param args: arg description
        :type args: type description
        """
        self._pkgs = args[:]
        args = self.pacman_args + args
        super(PacmanCmd, self).__init__(*args)
    # __init__()
# PacmanCmd

