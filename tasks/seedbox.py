# -*- coding: utf-8 -*-
from core.decorate import task
from core.utils import shell
from core.utils import shellquote
from termcolor import colored, cprint
import os

SEEDBOX_LOCAL = "~/Seedbox"
SEEDBOX_REMOTE_DOWNLOADS = "torrents/downloads"
SEEDBOX_REMOTE_SYNC = "torrents/sync"

@task(description="test",group="seedbox")
def fetch():
	# read log file and remove all existing in the log file
	log_file = shell( "ssh seedbox 'cat ~/%s/.synclog'" %SEEDBOX_REMOTE_SYNC, pipe=True )[0]
	log_file = log_file.split("\n")

	already_synced = []
	for i in range( 0, len(log_file) ):
		# check we have an actual log file by checking for "sync_log" string ( for first run )
		if i == 0 and log_file[i] != "sync_log":
			# otherwise create log file.
			createlog = "ssh seedbox 'echo \"%s\" >> ~/%s/.synclog'" %("sync_log",SEEDBOX_REMOTE_SYNC)
			cprint ( "first run...", "magenta" )
			cprint ( createlog, "green" )
			shell( createlog )
			break
		else:
			# otherwise add all files to files list for exclusion
			already_synced.append( log_file[i] )

	# get listing of download folder
	downloads = shell( "ssh seedbox 'ls ~/%s'" %SEEDBOX_REMOTE_DOWNLOADS, pipe=True )[0]
	downloads = downloads.split( "\n" )

	to_sync = []
	cprint ( "create symlinks...", "magenta" )
	for d in downloads:
		if d != None and len(d)>0:
			try:
				already_synced.index( d )
			except ValueError:
				to_sync.append( d )
				symlink = "ssh seedbox 'ln -s ~/%s/%s ~/%s/'" %(SEEDBOX_REMOTE_DOWNLOADS, shellquote(d), SEEDBOX_REMOTE_SYNC)
				cprint( symlink, "green" )
				shell( symlink )			

	cprint ( "rsync...", "magenta" )
	# now run rsync on all files in sync folder with L flag ( for copy synlink data )
	shell( "rsync -avzL seedbox:~/%s/ %s" %(SEEDBOX_REMOTE_SYNC,SEEDBOX_LOCAL) )

	cprint ( "writing log...", "magenta" )
	for f in to_sync:
		if f != None and len(f) > 0:
			# and write the log file.
			writelog = "ssh seedbox 'echo %s >> ~/%s/.synclog'" %(shellquote(f),SEEDBOX_REMOTE_SYNC) 
			cprint( writelog, "green" )
			shell( writelog )

	cprint ( "cleaning up...", "magenta" )
	for f in to_sync:
		if f != None and len(f) > 0:
			# clean up symlinks
			cleanup = "ssh seedbox 'rm ~/%s/%s'" %(SEEDBOX_REMOTE_SYNC,shellquote(f))
			cprint( cleanup, "green" )
			shell( cleanup )

	cprint( "done...", "magenta" )
	
