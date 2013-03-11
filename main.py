# -*- coding: utf-8 -*-
from tasks import *
from core.models import TaskManager
from termcolor import colored, cprint
import sys
from optparse import OptionParser


# parse options
parser = OptionParser()
parser.add_option( "-s", "--show", default=False, action="store_true", dest="show", help="display all tasks by group" )
#arser.add_option( "-d", "--dry-run", default=False, action="store_true", dest="dryrun", help="pass dry run flag to task" )
( options, args ) = parser.parse_args()

# check show first.
if options.show:
	groups = args
	if len( groups ):
		pass # print just groups.
	else:
		TaskManager.printAllTasks()
else:
	# run tasks.
	group = None
	tasks = []

	# check group supplied
	if len( args ) > 0:
		name = args[0]
		if TaskManager.hasGroup(name):
			group = name
			tasks = args[1:]
		else:
			tasks = args

	# validate and check tasks exist
	for task in tasks:
		if group:
			if TaskManager.hasGroupTask(group,task):
				print "run task " + task
				TaskManager.runTask(group,task)
			else:
				print "task '%s' in group '%s' not found." %(task,group)
		else:
			if TaskManager.hasTask(task):
				print "run task " + task
				TaskManager.runTask(None,task)
			else:
				print "task '%s' not found." %task
