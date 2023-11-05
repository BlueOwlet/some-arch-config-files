#!/bin/bash

. menu.sh


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

    sudo rm /etc/nginx/sites-enabled/*

    sudo cp backup/nginx/* /etc/nginx/sites-available/
    cd /etc/nginx/sites-enabled
    sudo ln -s ../sites-available/* .
    cdw

    sudo systemctl restart nginx
    sudo systemctl reload nginx
}


nginx_menu(){
    menu "nginx.sh"
}