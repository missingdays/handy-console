#! /bin/sh
#
# cpbin.sh
# Copyright (C) 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.
#

mkdir ~/.handy-console
git clone https://github.com/github/gitignore.git ~/.handy-console/ignores 
mv ~/.handy-console/ignores/Global/* ~/.handy-console/ignores
rm -rf ~./handy-console/ignores/Global
