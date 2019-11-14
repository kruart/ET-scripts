#!/usr/bin/python

import subprocess

# command = "code ."	# run vscode at current path
command = "pstree"

subprocess.Popen(command, shell=True)

#process open Popen 
