# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  config.vm.box = "raring64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/raring/current/raring-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.hostname = "devstack"
  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 6080, host: 6080 # vnc

  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", "2500"]
    v.customize ["modifyvm", :id, "--uart1", "0x3F8", 4]
  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "devstack.yml"
      ansible.inventory_file = "ansible_hosts"
      ansible.verbose = true
  end

end
