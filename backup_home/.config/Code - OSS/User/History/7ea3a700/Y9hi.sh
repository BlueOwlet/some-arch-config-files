#!/bin/bash
. menus.sh


install_podman(){

    sudo apt-get install -y podman
}

install_podman_docker(){
    sudo apt-get install -y podman-docker
}

install_docker_compose(){
    sudo curl -SL https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose version


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