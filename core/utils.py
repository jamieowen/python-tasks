# -*- coding: utf-8 -*-

import subprocess

def shell(command, pipe=False):
	"""
	Quick helper method to call a shell command.
	"""
	if pipe:
		process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE)
		return process.communicate()
	else:
		process = subprocess.Popen(command, shell=True,stderr=subprocess.STDOUT)
		process.wait()
		return None


def shellquote(s):
    return "\"" + s.replace("'", "'\\''") + "\""


	
	
	


