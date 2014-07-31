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
import sh
from sh import pacmans
from sh import yaourt
