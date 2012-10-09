#!/bin/sh

rpm -e --nodeps redhat-release-server-6Server
rpm -e --nodeps redhat-release-notes redhat-release yum-rhn-plugin redhat-logos
yum install -y centos-release
yum reinstall -y centos-release

exit 0
