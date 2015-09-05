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
