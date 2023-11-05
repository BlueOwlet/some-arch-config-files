#!/bin/bash

. ./menu.sh


install_and_enable_nginx(){

    sudo apt-get install nginx
    sudo systemctl start nginx
    sudo systemctl enable nginx

}


backup_nginx(){

}

restore_nginx


nginx_menu(){
    menu "nginx.sh"
}