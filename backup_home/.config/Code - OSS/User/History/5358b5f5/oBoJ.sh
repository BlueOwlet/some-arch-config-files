#!/bin/bash
. menu.sh


install_docker(){

    sudo apt-get install -y docker
}


install_docker_compose(){
    sudo apt-get install -y docker-compose
}





refresh_docker(){
    sudo docker images ps
    sudo docker container ps -a
    sudo docker stop -a
    sudo docker container rm -fa
    sudo docker rmi -fa
    sudo docker network rm jitsi_meet.jitsi
}

remove_podman(){
    sudo apt-get remove --purge docker-ce docker-ce-cli containerd.io}
    sudo rm -rf /var/lib/docker
    sudo apt-get remove --purge podman podman-docker podman-compose
    sudo rm -rf /var/lib/containers
}

veth_driver(){

    sudo apt-get install linux-headers-$(uname -r)
    ls /lib/modules/$(uname -r)/kernel/drivers/net/veth.ko

    sudo modprobe veth
    lsmod | grep veth
    
}


full_reinstall(){
refresh_podman
remove_podman
veth_driver
install_podman
restore_podman
install_podman_docker
install_podman_compose
# install_container_networking_plugins

}

podman_menu(){
    menu "podman.sh"
}
