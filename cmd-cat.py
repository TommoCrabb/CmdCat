#!/usr/bin/env python3
'''
This is intended to be a short and simple script which builds a
shell command from a config file. I originally wrote it because 
QEMU doesn't accept config files.
'''
from subprocess import run
from argparse import ArgumentParser

ap = ArgumentParser(
    description="""Takes a number of files as arguments, and 
    concatenates all lines into a single shell command. Empty
    lines and lines starting with "#" are ignored. By default,
    commands are printed to stdout but not run.
    Shell substitutions, such as "~/" will not work.
    """
)
ap.add_argument(
    "--run", "--execute", "-x", "-r", "-e",
    action="store_true",
    help="Run the command."
)
ap.add_argument(
    "files",
    nargs="+",
    help="""A list of configuration files whose lines will
    be concatenated together."""
)
args = ap.parse_args()

cmd = []
for x in args.files:
    with open(x, "r") as f:
        for l in f:
            l = l.split()
            if l and l[0] != "#":
                cmd.extend(l)

if args.run == True:
    run( cmd )
else:
    print( " ".join(cmd) )