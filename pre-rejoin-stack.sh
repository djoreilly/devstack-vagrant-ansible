#!/bin/bash

# run after reboot and before rejoin-stack.sh

set -x

# this file is used to back the stack-volumes VG used by cinder
sudo losetup -f /opt/stack/data/stack-volumes-backing-file

# following lines are only needed with the Open vSwitch agent
# ip link set dev br-ex up
# ip address add 172.24.4.225/28 dev br-ex
