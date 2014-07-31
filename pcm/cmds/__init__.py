import sys
import os
import importlib
import glob


# Imoprt and instantiate each Cmd object.
_this_dir = os.path.dirname(__file__)
_this_mod = os.path.basename(_this_dir)


def build_cmds(sub_parser):

    cmd_objs = {}
    imlist = glob.glob(os.path.join(_this_dir, "*.py"))
    imlist.remove(os.path.join(_this_dir, "__init__.py"))
    imlist.remove(os.path.join(_this_dir, "base.py"))

    imlist = [os.path.basename(x) for x in imlist]
    imlist = [os.path.splitext(x)[0] for x in imlist]

    # s = importlib.import_module('cmds.search')
    # print(s.Cmd.name)

    for im in imlist:
        # print(im)
        mod = importlib.import_module("pcm." + _this_mod + '.' + im)
        if hasattr(mod, 'Cmd'):
            # print("Found Command: ", mod.Cmd.name)
            cmd_objs[mod.Cmd.name] = mod.Cmd(sub_parser)
            cmd_objs[mod.Cmd.name].build()
    # end for im in imlist
    # print(cmd_objs)

    return cmd_objs
#build_cmds()
