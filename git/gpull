#!/usr/bin/python

import sys

import handy_utils as utils

from getopt import getopt

out = "git pull".split()

if len(sys.argv) == 1:
    out.append("origin")
    out.append("master")
elif len(sys.argv) == 2:
    out.append("origin")
    out.append(sys.argv[1])
elif len(sys.argv) == 3:
    out.append(sys.argv[1])
    out.append(sys.argv[2])

utils.call(out)
