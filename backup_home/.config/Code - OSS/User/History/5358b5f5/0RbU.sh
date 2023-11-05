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

remove_docker(){
    sudo apt-get remove --purge docker docker-ce docker-ce-cli containerd.io}
    sudo rm -rf /var/lib/docker
    sudo apt-get remove --purge docker-compose
    sudo rm -rf /var/lib/containers
}

veth_driver(){

    sudo apt-get install linux-headers-$(uname -r)
    ls /lib/modules/$(uname -r)/kernel/drivers/net/veth.ko

    sudo modprobe veth
    lsmod | grep veth
    
}


full_reinstall(){.
    remove_docker
    install_docker
    install_docker_compose


}

docker_menu(){
    menu "podman.sh"
}
