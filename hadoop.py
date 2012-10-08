from fabric.api import *

#----
@task
def hadoop_1_node_start():
	run('hadoop-daemon.sh start datanode')
	run('hadoop-daemon.sh start tasktracker')

@task
def hadoop_1_node_stop():
	run('hadoop-daemon.sh stop tasktracker')
	run('hadoop-daemon.sh stop datanode')

@task
def hadoop_1_master_start():
	run('hadoop-daemon.sh start namenode')
	run('hadoop-daemon.sh start jobtracker')

@task
def hadoop_1_master_stop():
	run('hadoop-daemon.sh stop jobtracker')
	run('hadoop-daemon.sh stop namenode')

# vim:ts=2 sts=2 ai
