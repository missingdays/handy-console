#!/usr/bin/python

import sys, getopt
from handy_utils import call
out = "git log --all --pretty=oneline --abbrev-commit --graph --decorate".split()

if len(sys.argv) != 1:

    for i in range(len(sys.argv)):
        flag = sys.argv[i]
        if flag == "-l":
            out.append("--not")
            out.append("--remotes")
            sys.argv.pop(i)

    out = out + sys.argv[1:]
call(out)
