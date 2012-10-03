#!/bin/sh

yum update -y 2>&1 | tee /tmp/yum.log-$(date +%Y%m%d_%H%M%S)
