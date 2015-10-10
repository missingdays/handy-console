#!/usr/bin/python

from handy_utils import call, append_args
import sys

out = "git diff --word-diff".split()
out = append_args(out, sys.argv[1:])

call(out)
