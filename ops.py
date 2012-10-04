from fabric.api import *

@task
def rsync_yum_repos():
	local('rsync -e ssh -av --delete /etc/yum.repos.d %s:/etc' % env.host)	

@task
def rsync_yum_conf():
	local('rsync -e ssh -av --delete /etc/yum.conf %s:/etc' % env.host)	

# vim:ts=2 
