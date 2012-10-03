from fabric.api import *

@task
def rsync_yum_repos():
	local('rsync -e ssh -av --delete /etc/yum.repos.d %s:/etc' % env.host)	

# vim:ts=2 
