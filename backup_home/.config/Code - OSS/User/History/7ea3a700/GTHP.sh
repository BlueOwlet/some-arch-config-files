#!/bin/bash
. menu.sh


install_podman(){

    sudo apt-get install -y podman
}

install_podman_docker(){
    sudo apt-get install -y podman-docker
}


start_podman_socket(){
    sudo systemctl enable --now podman.socket
    sudo systemctl status podman.socket
    sudo systemctl enable --now podman.socket

}

install_podman_compose(){
    sudo apt-get install -y python3-pip
    sudo pip install podman-compose 
    # podman-compose version
}


install_container_networking_plugins(){
    sudo apt install containernetworking-plugins
    sudo apt update
    podman system reset --force

}

backup_podman(){
    mkdir -p backup/podman
    sudo cp /etc/containers/registries.conf backup/podman/ 

}

restore_podman(){
    sudo cp backup/podman/registries.conf /etc/containers/
}


refresh_podman(){

    sudo podman images ps
    sudo podman container ps -a
    sudo podman stop -a
    sudo podman container rm -fa
    sudo podman rmi -fa
    sudo podman network rm jitsi_meet.jitsi
    sudo systemctl restart podman


    podman images ps
    podman container ps -a
    podman stop -a
    podman container rm -fa
    podman rmi -fa
    podman network rm jitsi_meet.jitsi

    #THIS IS SO PORTS DON'T STAY BINDED to rootlessport PROCESS
    pkill containers-rootlessport

}

remove_podman(){
    sudo apt-get remove --purge docker-ce docker-ce-cli containerd.io}
    sudo apt remove --purge docker-ce docker-ce-cli containerd.io}
    sudo rm -rf /var/lib/docker
    sudo apt-get remove --purge podman podman-docker podman-compose
    sudo apt remove --purge podman podman-docker podman-compose
    sudo rm -rf /var/lib/containers

    sudo apt-get autoclean && sudo apt autoremove
    sudo apt autoclean && sudo apt autoremove
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
