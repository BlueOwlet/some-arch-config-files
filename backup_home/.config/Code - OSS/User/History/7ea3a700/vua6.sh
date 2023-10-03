#!/bin/bash
. menus.sh


install_podman(){

    sudo apt-get install -y podman
}

install_docker_compoose(){
    sudo apt-get install -y podman-docker
}





podman_menu(){
    menu "podman.sh"
}