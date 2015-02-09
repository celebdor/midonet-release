#!/bin/bash

original_perms=`stat -c %u:%g /root/rpmbuild/SOURCES/*.spec`
chown root:root -R /root/rpmbuild/SOURCES
rpmbuild "$@"
chown $original_perms -R /root/rpmbuild/
