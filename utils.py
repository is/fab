import csv
import time

from fabric.api import *


def __append_hostdb(db, key, h):
	if key in db:
		db[key].append(h)
	else:
		db[key] = [h,]


def __build_hostdb(fn):
	DB = {}
	io8id = {}
	io8idr = {}

	fin = file(fn)
	cin = csv.reader(fin)

	for row in cin:
		hostname = row.pop(0)
		if hostname.startswith('#'):
			continue

		__append_hostdb(DB, 'all', hostname)
		
		for c in row:
			if c.find('{') != -1 or c.find('=') != - 1 or c.find(':') != -1:
				continue
			__append_hostdb(DB, c, hostname)
			if c.startswith('I__'):
				__append_hostdb(DB, c[3:], hostname)
				io8id[c[3:]] = hostname
				io8idr[hostname] = c[3:]

	env.io8id = io8id
	env.io8idr = io8idr

	fin.close()
	return DB

env.roledefs = __build_hostdb('/root/.fabric/hosts')


#----
def set_env_for_script(fn, env):
	fin = file(fn, 'r')
	lines = fin.readlines()
	fin.close()

	for line in lines:
		optline = None
		if line.startswith('// -- fabric.'):
			optline = line[13:]
		elif line.startswith('# -- fabric.'):
			optline = line[12:]

		if not optline:
			continue

		key, sep, value = optline.partition('=')
		key = key.strip()
		value = value.strip()
		if key == 'roles':
			value = value.split(',')

		if key == 'user':
			setattr(env, key, value)
		elif getattr(env, key) == None:
			setattr(env, key, value)

# vim:ts=2 sts=2 ai
