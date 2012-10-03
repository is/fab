import time, csv
from fabric.api import *

import hostsdb

import ops


def verify_hostname():
	run ('hostname')

@task(alias='R')
def run_sh(cmd):
	'''Run shell script on remote machines by SSH'''
	fn = '/tmp/%s_%s' % (cmd.replace('/', '__'), int(time.time()))
	put (cmd, fn, mode = 0700)
	run (fn)

# vim:ts=2
