from fabric.api import *
from fabric.contrib.project import *


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

#----
@task
def install_java_7():
	run('mkdir -p /is')
	rsync_project('/is/java', '/is/java-deploy/', delete=True, extra_opts='-a')
	put('resource/java7.sh', '/etc/profile.d/java7.sh')

# vim:ts=2 ai
