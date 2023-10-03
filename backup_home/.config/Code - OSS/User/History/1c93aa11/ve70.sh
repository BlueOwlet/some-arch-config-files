#!/bin/bash

. ./menu.sh


install_and_enable_nginx(){

     apt-get install nginx
     systemd-run start nginx
     systemd-run enable nginx

}

backup_nginx_sites_available(){
    echo "BACKING UP NGINX SITES AVAILABLE"
     cp /etc/nginx/sites-available/vyda.mx backup/nginx/
}

restore_nginx_sites_available(){
    echo "RESTORING NGINX SITES AVAILABLE"
     cp /backup/nginx/vyda.mx /etc/nginx/sites-available/
}

reload_nginx(){
     systemd-run reload nginx
     systemd-run restart nginx
}

nginx_menu(){
    menu "nginx.sh"
}