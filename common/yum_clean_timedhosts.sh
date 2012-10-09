#!/bin/sh

find /var/cache/yum -iname 'timedhosts.txt' -exec rm -f {} \;
