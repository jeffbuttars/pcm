import logging
logger = logging.getLogger('pcm')
import datetime
import dateutil.parser
import os

from pcm.cmds.base import BaseCmd
from pcm.lib.cmd import PacmanCmd


class Cmd(BaseCmd):
    """Docstring for Cmd """

    name = 'sync'
    help_text = ("Sync the repos")
    aliases = ('makecache',)

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            '-e', '--expired',
            default=False,
            action='store_true',
            help=("Only sync if sync time has expired"),
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

        sync = SyncCmd(if_expired=args.expired)
        sync.execute()
    # exec()
# Cmd


class SyncCmd(PacmanCmd):
    pacman_args = ('-Sy',)
    sync_time_file = '.pcm_last_sync'

    def __init__(self, if_expired=False, interval=86400):
        """
        if_expired is True, sync will only happen
        if the sync expire interval has passed.

        :param *pkgs: arg description
        :type *pkgs: type description
        """
        super(SyncCmd, self).__init__()

        self._if_expired = if_expired
        self._interval = interval
    # __init__()

    def _should_run(self):
        """todo: Docstring for _should_run
        :return:
        :rtype:
        """
        if not self._if_expired:
            return True

        if not os.path.isfile(self.sync_time_file):
            self.pr_info("There is no previous sync time.")
            return True

        last_sync = None
                
        with open(self.sync_time_file, 'r') as fd:
            last_sync = fd.read()
            last_sync = dateutil.parser.parse(last_sync)
            now = datetime.datetime.now()

            if (now - last_sync).seconds > self._interval:
                self.pr_info("Last sync was at %s, syncing" % last_sync)
                return True

        self.pr_info("Last sync was at %s, not syncing until after %s" % (
            last_sync, last_sync + datetime.timedelta(seconds=self._interval)))
        False
    # _should_run()

    def execute(self):

        if self._should_run():
            super(SyncCmd, self).execute()

            with open(self.sync_time_file, 'w') as fd:
                fd.write(datetime.datetime.now().isoformat())
    # execute()
# SyncCmd


class SyncFirst(PacmanCmd):
    def execute(self):
        sync = SyncCmd(if_expired=True)
        sync.execute()
        super(SyncFirst, self).execute()
    # execute()
# SyncFirst
