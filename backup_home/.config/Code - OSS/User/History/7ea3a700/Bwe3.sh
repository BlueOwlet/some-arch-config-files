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
sudo apt-get remove --purge docker-ce docker-ce-cli containerd.io}
sudo rm -rf /var/lib/docker
sudo apt-get remove --purge podman
sudo rm -rf /var/lib/containers



podman_menu(){
    menu "podman.sh"
}
