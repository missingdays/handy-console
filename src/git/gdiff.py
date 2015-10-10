#!/usr/bin/python

from handy_utils import call
import sys

out = "git diff --word-diff".split()
out = out + sys.argv[1:]

call(out)
