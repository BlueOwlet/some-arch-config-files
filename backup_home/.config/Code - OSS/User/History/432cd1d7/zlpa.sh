#!/bin/bash

. ./menu.sh


install_and_enable_nginx(){

    sudo apt-get install nginx
    sudo systemctl start nginx
    sudo systemctl enable nginx

}

backup_nginx_sites_available(){
    echo "BACKING UP NGINX SITES AVAILABLE"
    sudo cp /etc/nginx/sites-available/vyda.mx .
}

restore_nginx_sites_available(){
    echo "RESTORING NGINX SITES AVAILABLE"
    sudo cp vyda.mx /etc/nginx/sites-available/
}



nginx_menu(){
    menu "nginx.sh"
}