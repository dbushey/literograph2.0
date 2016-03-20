Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provision "shell", path: "setup.sh", privileged: false

  config.vm.network :forwarded_port, host: 8080, guest: 80
  config.vm.network :forwarded_port, host: 8000, guest: 8001

  # Uri's Change - sync folders from host to guest VM
  config.vm.synced_folder ".", "/home/vagrant"

end



