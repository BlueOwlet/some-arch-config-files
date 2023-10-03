#!/bin/bash
. menus.sh


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
    podman images ps
    podman stop --all
    podman container list
    podman container rm -a
    podman rmi --all
    podman images rmi -a
    podman network rm jitsi_meet.jitsi
    sudo systemctl restart podman
}

full_reinstall(){

refresh_podman
sudo apt-get remove --purge docker-ce docker-ce-cli containerd.io}
sudo rm -rf /var/lib/docker
sudo apt-get remove --purge podman podman-docker podman-compose
sudo rm -rf /var/lib/containers
install_podman
install_podman_docker
install_podman_compose
# install_container_networking_plugins

}

podman_menu(){
    menu "podman.sh"
}
