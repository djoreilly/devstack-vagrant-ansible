#!/usr/bin/python
'''
create a Nova "keypair" based on id_rsa.pub

then you can just do:
$ ssh user@instance_ip

as ssh tries ~/.ssh/id_rsa if there is no "-i" on command line
'''

import os
import shlex
import socket
import subprocess
import sys
import novaclient.client

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d


nc = novaclient.client.Client('1.1', **get_nova_creds())

key_name = socket.gethostname()
try:
    key = nc.keypairs.find(name=key_name)
    print "key %s already imported Nova: %s" %(key_name, key.id)

    sys.exit(0)

except novaclient.client.exceptions.NotFound:
    pass

prv_key_path = os.path.expanduser('~/.ssh/id_rsa')
pub_key_path = prv_key_path + '.pub'
if not os.path.exists(prv_key_path):
    print "%s not found, creating keypair" %prv_key_path
    cmdline = 'ssh-keygen -t rsa -N "" -f %s' % prv_key_path
    args = shlex.split(cmdline)
    subprocess.check_output(args)

with open(pub_key_path, 'r') as f:
    pub_key = f.read()

key = nc.keypairs.create(name=key_name, public_key=pub_key)

print "created keypair: %s id = %s" % (key_name, key.id)

