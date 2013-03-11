# -*- coding: utf-8 -*-
import inspect
from termcolor import cprint

class TaskItem():
	"""
	Wraps a task function in to an object for easier use.
	"""
	def __init__(self,args,kwargs,taskFunc):
		"""
		Initialises from the task decorator  maker below.
		"""
		self.args 	= args
		self.kwargs = kwargs
		self.task 	= taskFunc
		self.name 	= taskFunc.__name__

		if kwargs.has_key( "group" ):
			self.group = kwargs["group"]
		else:
			self.group = "none"

		if kwargs.has_key( "description" ):
			self.description = kwargs["description"]
		else:
			self.description = "--no description--"

	def execute(self):
		"""
		executes the task function.
		"""
		self.task()

	def __str__(self):
		"""
		String version of task
		"""
		return self.name


class TaskManager():
	"""
	Singleton manages all tasks added via the @task syntax.
	"""
	tasks = tasks = []

	@staticmethod
	def getTasksByGroup(group):
		"""
		Get all tasks filtered by group.
		"""
		return [ task for task in TaskManager.tasks if task.group == group ]

	@staticmethod
	def getGroups():
		"""
		Get all groups.
		"""
		groups = {}
		for task in TaskManager.tasks:
			groups[task.group] = True

		return groups.keys()

	@staticmethod
	def hasGroup(name):
		groups = TaskManager.getGroups()
		try:
			groups.index(name)
			return True
		except ValueError:
			return False

	@staticmethod
	def hasTask(name):
		return len( [task for task in TaskManager.tasks if task.name == name] ) > 0

	@staticmethod
	def hasGroupTask(group,task):
		if TaskManager.hasGroup(group):
			tasks = TaskManager.getTasksByGroup( group )
			return len( [t for t in tasks if t.name == task ] ) > 0
		else:
			return False

	@staticmethod
	def getTasks():
		"""
		Return all tasks.
		"""
		return tasks

	@staticmethod
	def getTask(name):
		if TaskManager.hasTask(name):
			return [task for task in TaskManager.tasks if task.name == name ][0]
		else:
			return None

	@staticmethod
	def getGroupTask( group, task ):
		tasks = TaskManager.getTasksByGroup( group )
		l = [t for t in tasks if t.name == task ]
		if len(l):
			return l[0]
		else:
			return None

	@staticmethod
	def getTask( task ):
		tasks = TaskManager.getTasks()
		l = len([t for t in tasks if t.name == task ])
		if l:
			return l[0]
		else:
			return None

	@staticmethod
	def addTask(task):
		TaskManager.tasks.append( task )

	@staticmethod
	def runTask(group,task):
		if group:
			task = TaskManager.getGroupTask( group, task )
			task.execute()
		else:
			task = TaskManager.getTask( task )

	@staticmethod
	def printAllTasks():
		for group in TaskManager.getGroups():
			tasks = TaskManager.getTasksByGroup(group)
			cprint ( group, "yellow" )
			for i in range(0,len(tasks),3):
				if i+2 < len(tasks):
					cprint ( "%-25s %-25s %-25s" %(tasks[i], tasks[i+1], tasks[i+2]), "blue" )
				elif i+1 < len(tasks):
					cprint ( "%-25s %-25s" %(tasks[i], tasks[i+1]), "blue" )
				else:
					cprint ( "%-25s" %(tasks[i]), "blue" )

