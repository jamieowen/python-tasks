# -*- coding: utf-8 -*-
from models import *

def task(*args,**kwargs):
	"""
	Defines the task decorator setup.
	For using @task syntax in files found in the tasks/ folder.
	"""
	def decorator(taskFunc):
		task = TaskItem(args,kwargs,taskFunc)
		TaskManager.addTask( task )

		#def empty():
		#	pass

		return taskFunc

	return decorator