#!/bin/bash

# run after reboot and before rejoin-stack.sh

set -x

losetup -f /opt/stack/data/stack-volumes-backing-file
ip link set dev br-ex up
ip address add 172.24.4.225/28 dev br-ex
