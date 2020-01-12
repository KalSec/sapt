#!/usr/bin/env python3

from argparse import ArgumentParser
import sys

usage = "sapt [options] "
Version = "sapt 0.0.1"

def arguments():
    parser = ArgumentParser(usage=usage, description="SAPT is an penetration testing tool used to automate the normal or common taks", epilog="Hope you are happy with this tool.")
    parser.version = Version
    parser.add_argument('-t', '--target', metavar='', help="specify Target for scan")
    parser.add_argument('-V', '--verbose', action='store_true', dest='verbose', help="Displays more information.")
    parser.add_argument('-e', '--enumerate', metavar='', help="Displays more information.")
    parser.add_argument('--version', action='version')
    args = parser.parse_args()

# verifying the arguments

    if not len(sys.argv) > 1:
        parser.print_help()

# Conditions with the options

    if args.target:
        print(args.target)
        sys.exit(0)


