#!/usr/bin/env python3

import os, sys, getpass

'''
Copyright (C) 2020, kal.
'''
# ascii art of sapt
def asciiArt():
	os.system("clear")
	print( '''

	                    ___    __    ____  ____
	                   / __)  /__\  (  _ \(_  _)
		           \__ \ /(__)\  )___/  )(
	                   (___/(__)(__)(__)   (__)

	          """Semi Automated Penetration Testing""" by kal
	''')


def isRoot():
	user = getpass.getuser()
	if not os.geteuid() == 0:
		sys.exit("\nHello, "+user+". \nOnly root can run this script.\nUse sudo or run as root.\n")

