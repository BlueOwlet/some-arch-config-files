#!/bin/bash

. ./menu.sh


install_nginx(){

    sudo apt-get install -y nginx-full

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
    nginx -s reload

}

uninstall_nginx(){
    sudo apt remove nginx 
    sudo apt-get purge nginx nginx-common nginx-full

    sudo rm -r /etc/nginx/

    sudo apt-get autoremove

    sudo apt-get remove --purge nginx*

    sudo apt-get autoremove --purge

    sleep 3
    sudo apt-get install nginx

    echo "nginx exists?"
    ls /etc/ | grep nginx
}

run_nginx_installation(){
    install_nginx
    enable_nginx
    

}

nginx_menu(){
    menu "nginx.sh"
}