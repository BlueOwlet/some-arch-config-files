#!/bin/bash

. ./menu.sh


install_and_enable_nginx(){

    sudo apt-get install nginx
    sudo systemctl start nginx
    sudo systemctl enable nginx

}


backup_nginx(){
    mkdir -p backup/nginx
    sudo cp /etc/nginx/sites-available/vyda.mx backup/nginx

}

restore_nginx(){
    sudo cp /etc/nginx/sites-available/vyda.mx

}


nginx_menu(){
    menu "nginx.sh"
}