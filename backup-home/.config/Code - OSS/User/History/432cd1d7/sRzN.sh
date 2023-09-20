#!/bin/bash

. ./menu.sh


install_nginx(){

    sudo apt-get install -y nginx

}

enable_nginx(){
    nginx
    nginx -s start
    nginx -s reload
    sudo systemctl start nginx
    sudo systemctl enable nginx
}


backup_nginx_sites_available(){
    echo "BACKING UP NGINX SITES AVAILABLE"
    sudo cp /etc/nginx/sites-available/* backup/nginx/
}

restore_nginx_sites_available(){
    echo "RESTORING NGINX SITES AVAILABLE"
    sudo cp backup/nginx/* /etc/nginx/sites-available/
}

reload_nginx(){
    sudo systemctl reload nginx
    sudo systemctl restart nginx
}

nginx_menu(){
    menu "nginx.sh"
}