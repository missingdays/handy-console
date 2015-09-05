#!/usr/bin/python

import sys, getopt
from handy_utils import call
out = "git log --all --pretty=oneline --abbrev-commit --graph --decorate".split()

if len(sys.argv) != 1:
    args, flags = getopt.getopt(sys.argv, "h")
    for flag in flags:
        if flag == "-u":
            out.append("-u")
        elif flag == "-l":
            out.append("--not")
            out.append("--remotes")

call(out)
