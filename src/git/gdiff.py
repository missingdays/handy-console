#!/usr/bin/python

from handy_utils import call
import sys

out = "git diff --word-diff".split()

call(out)
