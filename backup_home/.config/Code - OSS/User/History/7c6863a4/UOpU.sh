#!/bin/bash
. ./menu.sh


install_gunicorn(){
    sudo apt-get install gunicorn
    sudo systemctl start gunicorn 

}

restore_gunicorn_service_file(){
    sudo cp backup/gunicorn.service /etc/systemd/system/gunicorn.service

}



gunicorn_menu(){
    menu "gunicorn.sh"
}