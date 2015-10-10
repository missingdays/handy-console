#!/usr/bin/python

import sys

from handy_utils import call, append_args

out = "git push".split()

if len(sys.argv) == 1:
    out.append("origin")
    out.append("master")
elif len(sys.argv) == 2:
    out.append("origin")
    out.append(sys.argv[1])
elif len(sys.argv) == 3:
    out.append(sys.argv[1])
    out.append(sys.argv[2])

call(out)

