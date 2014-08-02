import logging
logger = logging.getLogger('pcm')

import os
import sys
import subprocess
# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO
import shutil
from urllib.parse import urlparse
from pprint import pformat as pf

from blessings import Terminal

from pcm.lib.exceptions import NoPacmanFound

PKGRS = {}
import sh
try:
    from sh import pacman
    PKGRS['pacman'] = pacman
except ImportError:
    raise NoPacmanFound()

# from sh import yaourt
# PKGRS['yaourt'] = yaourt

sh.logging_enabled = True

class Cmd(object):
    """Docstring for PkgrExec """

    def __init__(self, *args, command=None):
        """todo: to be defined

        :param pkgr: arg description
        :type pkgr: type description
        :param args: arg description
        :type args: type description
        """
        self._cmd = command
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
    #_build_writer()

    def _sh_stdout(self, *args, **kwargs):
        return self._build_writer(sys.stdout, *args, **kwargs)
    #_sh_stdout()

    def _sh_stderr(self, *args, **kwargs):
        return self._build_writer(sys.stderr, *args, **kwargs)
    #_sh_stderr()

    def pr_pass(self, fmt, *args, **kwargs):
        print(self.term.green(fmt.format(*args, **kwargs)))
    #pr_pass()

    def pr_info(self, fmt, *args, **kwargs):
        print(self.term.blue(fmt.format(*args, **kwargs)))
    #pr_info()

    def pr_fail(self, fmt, *args, **kwargs):
        print(self.term.red(fmt.format(*args, **kwargs)))
    #pr_fail()

    def pr_atten(self, fmt, *args, **kwargs):
        print(self.term.red(fmt.format(*args, **kwargs)))
    #pr_atten()

    @property
    def cmd(self):
        return self._cmd
    # cmd()

    def execute(self):
        logger.debug("%s %s", self._cmd, self._args)
        try:
            p = self._cmd(
                *self._args,
                _in=sys.stdin,
                _out=self._sh_stdout(),
                # _err=self._sh_stderr('red'),
                _err_to_out=True,
                _out_bufsize=0,
                _in_bufsize=0
                # _tty_out=False,
                # _tty_in=True
            )
            # print(dir(p))
            p.wait()
        except sh.ErrorReturnCode_1 as e:
            self.pr_fail("command '{} {}' failed", self._cmd, " ".join(self._args))
    # execute()
# Cmd


class PacmanCmd(Cmd):
    """Docstring for PkgrCmd """
    pacman_args = ()

    def __init__(self, *args):
        """todo: to be defined

        :param pkgr: arg description
        :type pkgr: type description
        :param args: arg description
        :type args: type description
        """
        self._pkgs = args[:]
        args = self.pacman_args + args
        super(PacmanCmd, self).__init__(*args, command=pacman)
    # __init__()
# PacmanCmd
