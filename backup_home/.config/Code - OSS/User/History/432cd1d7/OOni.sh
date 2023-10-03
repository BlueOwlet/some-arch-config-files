#!/bin/bash

. ./menu.sh


install_nginx(){

    sudo apt-get install nginx
    sudo systemctl start nginx
    sudo systemctl enable nginx

}

