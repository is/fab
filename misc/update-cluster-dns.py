from fabric.api import *

#
# Update dns data in batch mode.
#
# Usage:
# fab -f misc/update-cluster-dns
# 

@hosts('pupili')
def update_pupil():
	prefix='/var/named/root'
	target = prefix + '/zz/io8.org.hadoop'
	script = prefix + '/fresh-zone-serial'
	put('/tmp/io8.org.hadoop', target)
	run('chown -R nobody:nobody %s' % target)

	put('misc/__fresh-zone-serial', script, mode=755)
	with cd(prefix):
		run('%s io8.org' % script)
	run('service named reload')
	run('rm -fr %s' % script)

@task(default=True)
def update_dns():
	local('python misc/gendnszone.py > /tmp/io8.org.hadoop')
	execute(update_pupil)


# vim:ts=2 sts=2 ai
