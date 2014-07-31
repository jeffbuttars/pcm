#!/usr/bin/env python
# encoding: utf-8

import logging

# Set up the logger
logger = logging.getLogger('pcm')
# Use a console handler, set it to debug by default
logger_ch = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter(
    ('%(levelname)s: %(asctime)s %(processName)s:%(process)d'
     ' %(filename)s:%(lineno)s %(module)s::%(funcName)s()'
     ' -- %(message)s'))
logger_ch.setFormatter(log_formatter)
logger.addHandler(logger_ch)

import sys
import os

if __name__ == '__main__':
    this_dir = os.path.realpath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.abspath(os.path.join(this_dir, "../")))

import argparse
from pcm import cmds

parser = argparse.ArgumentParser(
    "pcm",
    description=("Pacman Command Master")
)

parser.add_argument('-d',
                    '--debug',
                    default=False, action='store_true',
                    help=("Enable debug output and debug run mode")
                    )

# parser.add_argument('-c',
#                     '--config',
#                     default=None,
#                     help=("Specify a config file location.")
#                     )

def main():
    sub_parser = parser.add_subparsers(help=("pcm commands"))
    cmds.build_cmds(sub_parser)

    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)
        cmd_logger.setLevel(logging.DEBUG)

    logger.debug("args: %s", args)

    # import conf
    # conf.load_settings(args.config)

    logger.debug("settings: %s", conf.settings)

    if hasattr(args, 'func'):
        return args.func(args)
    parser.print_help()
# main()

if __name__ == '__main__':
    main()
