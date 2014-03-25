# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  # forward ssh keys from main host - handy for gerrit and github
  config.ssh.forward_agent = true

  # ubuntu precise because it's what OpenStack CI uses
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.hostname = "devstack"

  # eth1 will be the primary interface for access to the vagrant box.
  # It's plugged into a virtualbox bridge, so its IP can be accessed
  # directly from the main host without nat port-forwarding hassle.
  # All OpenStack services will be available on this address.
  config.vm.network :private_network, ip: "192.168.2.2"

  # Add eth2 and eth3 for linuxbridge-agent interface_mappings.
  # It's necessary to specify IPs here - but they are not configured.
  config.vm.network :private_network, ip: "192.168.3.2", auto_config: false
  config.vm.network :private_network, ip: "192.168.4.2", auto_config: false

  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--cpus", "2"]
    v.customize ["modifyvm", :id, "--memory", "4000"]
    # enable serial port just in case vagrant image does not
    v.customize ["modifyvm", :id, "--uart1", "0x3F8", 4]
  end

end
