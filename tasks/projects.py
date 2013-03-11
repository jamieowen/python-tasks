# -*- coding: utf-8 -*-
from core.decorate import task
import subprocess

@task(description="Cleans up projects", group="projects")
def projectTask1():
	print "projectTask1"
	process = subprocess.Popen("ls -la", shell=True)
	process.wait()

@task(name="Archives a specific project", group="projects")
def projectTask2(arg1="", arg2=""):
	print "projectTaskk"
	process = subprocess.Popen("du -ch", shell=True)
	process.wait()