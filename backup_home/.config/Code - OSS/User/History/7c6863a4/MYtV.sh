#!/bin/bash
. ./menu.sh


install_gunicorn(){
    sudo apt-get install gunicorn
    sudo systemctl start gunicorn 

}

restore_gunicorn_service_file(){
    sudo cp backup/gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service

}

restart_gunicorn(){
    sudo systemctl restart gunicorn
}



gunicorn_menu(){
    menu "gunicorn.sh"
}