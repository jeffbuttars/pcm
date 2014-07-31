import logging
logger = logging.getLogger('upkg')

import os
import sys
import subprocess
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
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
        self.cmd = command
    # __init__()

    def _build_writer(self, output, color=None, prefix=""):
        if color:

            def _cwriter(line):
                go = getattr(self.term, color)
                output(go(self.name + ": " + prefix + line))

            return _cwriter

        def _writer(line):
            output(self.name + ": " + prefix + line)

        return _writer
    #_build_writer()

    def _sh_stdout(self, *args, **kwargs):
        return self._build_writer(sys.stdout.write, *args, **kwargs)
    #_sh_stdout()

    def _sh_stderr(self, *args, **kwargs):
        return self._build_writer(sys.stderr.write, *args, **kwargs)
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

    def execute(self):
        p = self.cmd(args,
               _out=self._sh_stdout('blue'),
               _err=self._sh_stderr('red'))
        p.wait()
    # execute()
# Cmd


class PacmanCmd(Cmd):
    """Docstring for PkgrCmd """

    def __init__(self, *args):
        """todo: to be defined

        :param pkgr: arg description
        :type pkgr: type description
        :param args: arg description
        :type args: type description
        """
        self._pkgr_str = pkgr
        self._pkgr = PKGRS[pkgr]

        args = ['-S'] + args

        super(PacmanCmd, self).__init__(*args, command=pacman)
    # __init__()

    def __repr__(self):
        return "{} {}".format(
            self._pkgr,
            self._args,
        )
    # __repr__()

    def __str__(self):
        return self.__repr__()
    # __str__()


    @property
    def pkgr(self):
        logger.debug("pkgr: %s", self._pkgr)
        return self._pkgr
    # pkgr()

    # def execute(self):
    #     """todo: Docstring for execute
    #     :return:
    #     :rtype:
    #     """
    #     super(PacmanCmd, self).execute()
    # # execute()
# PacmanCmd
