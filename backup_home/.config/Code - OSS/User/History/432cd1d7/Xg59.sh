#!/bin/bash

. ./menu.sh


install_and_enable_nginx(){

    sudo apt-get install nginx
    sudo systemctl start nginx
    sudo systemctl enable nginx

}

backup_nginx_sites_available(){
    echo "BACKING UP NGINX SITES AVAILABLE"
    sudo cp /etc/nginx/sites-available/vyda.mx backup/nginx/
}

restore_nginx_sites_available(){
    echo "RESTORING NGINX SITES AVAILABLE"
    sudo cp /backup/nginx/vyda.mx /etc/nginx/sites-available/
}



nginx_menu(){
    menu "nginx.sh"
}