from fabric.api import *

@task
def rsync_yum_repos():
	local('rsync -e ssh -av --delete /etc/yum.repos.d %s:/etc' % env.host)	

@task
def rsync_yum_conf():
	local('rsync -e ssh -av --delete /etc/yum.conf %s:/etc' % env.host)	

@task
def set_is_hostid():
	io8id = env.io8idr[env.host]
	run('mkdir -p /is/etc')
	run('echo %s > /is/etc/hostid.is' % io8id)
	put('resource/is-hostid.sh', '/etc/profile.d')

# vim:ts=2 ai
