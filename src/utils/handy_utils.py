#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Utility functions
"""

import subprocess

def call(out):
    print(" ".join(out))
    subprocess.call(out)

def append_args(out, args):
    for arg in args:
        out.append(arg)
    return out    

if __name__ == "__main__":
    print(":P")
