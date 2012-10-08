#!/usr/bin/python
import csv
import socket

def gen_dns_zone_data(fn):
	fin = file(fn)
	cin = csv.reader(fin)

	for row in cin:
		hostname = row.pop(0)
		if hostname.startswith('#'):
			continue

		for c in row:
			if c.startswith('I__'):
				addr = socket.gethostbyname(hostname)
				hname = c[3:]
				print '%-30s IN  A        %s' % (hname, addr)

	fin.close()


if __name__ == '__main__':
	gen_dns_zone_data('/root/.fabric/hosts')
	
# vim:ts=2 sts=2 ai
