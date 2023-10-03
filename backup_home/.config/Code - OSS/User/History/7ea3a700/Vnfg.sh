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
    podman rm -a
    podman images rm -a

}



podman_menu(){
    menu "podman.sh"
}