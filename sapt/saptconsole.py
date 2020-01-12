#!/usr/bin/env python3

'''
Copyright (C) 2020, kal.
'''

import sys
from os import system
from lib.asciiart import *
from argparse import ArgumentParser

usage = "sapt [options] "
Version = "sapt 0.0.1"
parser = ArgumentParser(usage=usage, description="SAPT is an penetration testing tool used to automate the normal or common taks", epilog="Hope you are happy with this tool.")
parser.version = Version
parser.add_argument('-q', '--quiet', action='store_true', help="Disables the logo")
parser.add_argument('-V', '--verbose', action='store_true', dest='verbose', help="Displays more information.")
parser.add_argument('-e', '--enumerate', metavar='', help="Displays more information.")
parser.add_argument('--version', action='version')
args = parser.parse_args()
system("clear")
# printing Asciiart
if not args.quiet:
    asciiArt()
# Checking for root
isRoot()
