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

	fin.close()
	return DB

env.roledefs = __build_hostdb('/root/.fabric/hosts')
