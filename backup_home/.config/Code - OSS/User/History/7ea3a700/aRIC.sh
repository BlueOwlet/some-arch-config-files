#!/bin/bash
. menus.sh


install_podman(){

    sudo apt-get install -y podman
}





podman_menu(){
    menu "podman.sh"
}