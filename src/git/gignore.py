#!/usr/bin/python

import sys
from getopt import getopt
import os

def parse(f):
    s = f.split(".")
    return s[0].lower()

def list_lang(opts):
    print("Available ignores listing: ")
    if opts:
        for opt in opts:
            if opt in ignores:
                print("    " + opt + " is available")
            else:
                print("    " + opt + " is not available. Consider contibuting")
    else:
        for lang in ignores:
            print("    " + lang)

def should_ignore_file(filename):
    return filename.startswith(".")

def usage():
    print("""
usage: gignore [flags]* [language]+
flags:
    -h to get help
    -l to list all available ignores
    """)

def init_ignores():
    ignores = {}
    path = os.path.expanduser("~") + "/.handy-console/ignores"

    for filename in os.listdir(path):
        if should_ignore_file(filename):
            continue
        with open(path + "/"  + filename, 'r') as f:
            ignores[parse(filename)] = f.read()
    return ignores

def main():
    if len(sys.argv) == 1 or sys.argv[1] == "-h":
        usage()
    elif sys.argv[1] == "-l":
        list_lang(sys.argv[2:])
    else:
        ignores = init_ignores()
        with open(".gitignore", "a") as f:
            opts, args = getopt(sys.argv, "h")

            for arg in args[1:]:
                if arg in ignores:
                    f.write("\n# " + arg + "\n")
                    f.write(ignores[arg])
                    f.write("\n")
                else:
                    print("Can't find pattern for " + arg)
                    print("Please suggest contributing to project. More info in README")

if __name__ == "__main__":
    main()
