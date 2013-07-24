devstack-vagrant-ansible
========================

Builds a new Ubuntu Raring (13.04) VM, installs git and clones devstack and copies a localrc. 

Requirements
-----------

* Vagrant 1.2
* [Ansible](http://www.ansibleworks.com/)
* VirtualBox


Steps
-----

    git clone https://github.com/djoreilly/devstack-vagrant-ansible.git stack
    cd stack
    vagrant up

After it boots:

    vagrant ssh
    cd devstack
    ./stack.sh
