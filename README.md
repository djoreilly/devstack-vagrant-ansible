devstack-vagrant-ansible
========================

Builds a new Ubuntu Precise (12.04) VM, installs some prereqs and clones [devstack](http://devstack.org/) and provides a localrc. The localrc is for the Neutron ML2 plugin with the linuxbridge-agent - this is much simpler than the Open vSwitch agent.


Requirements
------------

* Vagrant
* [Ansible](http://www.ansibleworks.com/)
* VirtualBox
* git


Steps
-----

    host$ git clone https://github.com/djoreilly/devstack-vagrant-ansible.git stack
    host$ cd stack
    host$ vagrant up

after it boots, login an update the packages:

    host$ vagrant ssh
    vagrant@devstack:~$ sudo apt-get update && sudo apt-get --yes dist-upgrade

and reboot:

    host$ vagrant reload

run an Ansible script to install some prereqs for devstack:

    host$ ansible-playbook -v devstack.yml

run devstack:

    vagrant@devstack:~$ cd devstack && ./stack.sh

Put the external subnet's gateway IP address on the Linux bridge for the external network. This will make the Vagrant VM the next-hop router for the Neutron router created by stack.sh, and allow comms with the instances using the SNAT gateway or floating IPs:

    vagrant@devstack:~$ /vagrant/put-gw-ip-ex-br



Optional
--------

If you want to share files using the /vagrant shared folder, you will need to rebuild the VirtualBox additions module for the new kernel:

    sudo apt-get install dkms
    sudo /etc/init.d/vboxadd setup


Or NFS mount /opt/stack on the host. This is handy for GUI editing from the host

    sudo mount -o soft 192.168.2.2:/opt/stack /mnt/stack


Remove the default libvirt bridge and network

    sudo virsh net-destroy default
    sudo virsh net-undefine default


Remove unneeded ruby gems that this vagrantbox bundles

    for x in `gem list --no-versions`; do sudo gem uninstall $x -a -x -I; done


If using Gerrit or Github, update  ~/.gitconfig. See [configuring git-review](https://wiki.openstack.org/wiki/Gerrit_Workflow). Vagrant is already configured to forward the ssh keys.

    [color]
	    ui = auto
    [user]
	    name = firstname lastname
	    email = email-address
    [gitreview]
	    username = gerrit-username


os-loganalyze
-------------

View colorized log in a browser on main host instead of the screens. See [os-loganalyze](https://github.com/openstack-infra/os-loganalyze)

    cd /opt/stack/os-loganalyze
    sudo python setup.py install
    htmlify-server.py 1>/opt/stack/logs/screen/os-loganalyze.log 2>&1 &

If you get "setuptools>=0.8 is required for wheel installs. pip's wheel support requires" setuptools>=0.8.", do: "sudo pip install setuptools --upgrade"

Then the logs should be at http://192.168.2.2:8000/

