import os, sys
import time

from fabric.api import *

import utils
from utils import set_env_for_script

import ops


# --- local modules
import h4a
# --- end


@task(alias='VH')
def verify_hostname():
	"""Verify host up & output hostname"""
	run ('hostname')


def run_sh_oneline(cmd):
	run(cmd)

def run_sh_script(cmd):
	'''Run shell script on remote machines by SSH'''
	fn = '/tmp/%s_%s' % (cmd.replace('/', '__'), int(time.time()))
	put (cmd, fn, mode = 0700)
	run (fn)


@task(alias='R')
def run_sh(*argv):
	'''Run shell scripts on remote machines.'''
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
		set_env_for_script(fn, env)
		run_sh_script(fn)
		# Read Script from standard input
	elif cmd.startswith('>>>'):
		run_sh_oneline(cmd[3:])
	else:
		set_env_for_script(cmd, env)
		run_sh_script(cmd)

# vim:ts=2 ai
