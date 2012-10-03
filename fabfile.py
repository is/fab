import os, sys
import time

from fabric.api import *

import hostsdb

import ops

@task
def verify_hostname():
	"""Verify host up & output hostname"""
	run ('hostname')


@task
def run_sh_oneline(cmd):
	run(cmd)

@task(alias='R__')
def run_sh_script(cmd):
	'''Run shell script on remote machines by SSH'''
	fn = '/tmp/%s_%s' % (cmd.replace('/', '__'), int(time.time()))
	put (cmd, fn, mode = 0700)
	run (fn)

@task(alias='R')
def run_sh(*argv):
	if len(argv) == 0:
		cmd = None
	else:
		cmd = argv[0]

	if cmd == None:
		fn = "/tmp/run_sh_%s__%s" % (
			time.strftime('%Y%m%d-%H%M%S'), 
			os.getpid())

		fout = open(fn, 'w')
		fout.write(sys.stdin.read())
		fout.close()
		execute(run_sh_script, fn)
		# Read Script from standard input
	elif cmd.startswith('>>>'):
		execute(run_sh_oneline, cmd[3:])
	else:
		execute(run_sh_script, cmd)
		
		
# vim:ts=2 ai
