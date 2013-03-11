# -*- coding: utf-8 -*-
from core.decorate import task
from core.utils import shell

# Backup / Server Locations
SEEDBOX_SYNC 	= "jamieowen@seedbox.com:/sync"
SEEDBOX_DLS 	= "jamieowen@seedbox.com:/downloads"
LACIE 			= "/Volumes/LaCie"
GDRIVE			= "/Users/jamieowen/Google\ Drive"
DROPBOX			= "/Users/jamieowen/Dropbox"
SPENDRUPS   	= "jamie@jamieowen.com:"

# Local Locations for server backups or seedbox fetches.
SEEDBOX_LOCAL 	= "/Users/jamieowen/Seedbox"
SPENDRUPS_LOCAL = "/Users/jamieowen/Spendrups"

# Documents and work locations
WORKBENCH 		= "/Users/jamieowen/Workbench"
SYSTOOLS 		= "/Users/jamieowen/SystemTools"
PICTURES 		= "/Users/jamieowen/Pictures"
MOVIES 			= "/Users/jamieowen/Movies"
EBOOKS			= "/Users/jamieowen/EBooks"
AUDIOBOOKS		= "/Users/jamieowen/AudioBooks"
DESKTOP			= "/Users/jamieowen/Desktop"
DOWNLOADS 		= "/Users/jamieowen/Downloads"

APPSUPPORT 		= "/Users/jamieowen/Library/Application\ Support"

@task(description="Fetches new downloads from seedbox", group="sync")
def seedbox_fetch():
	print "seedbox_fetch"
	shell( "ls -la" )


@task(description="Backup to gdrive", group="sync")
def gdrive_backup():
	print "gdrive_backup" 
	shell( "ls -la" )



