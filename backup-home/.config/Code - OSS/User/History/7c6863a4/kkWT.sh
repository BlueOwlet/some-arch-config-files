#!/bin/bash
. ./menu.sh


install_gunicorn(){
    sudo apt-get install gunicorn

}

restore_and_start_gunicorn_with_service_file(){
    mkdir -p gunicorn
    sudo cp backup/gunicorn/gunicorn.service gunicorn/
    sudo cp backup/gunicorn/gunicorn-config.py gunicorn/
    sudo systemctl start gunicorn 

}

reload_gunicorn(){
    sudo cp backup/gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
}

restart_gunicorn(){
    sudo systemctl restart gunicorn
}



gunicorn_menu(){
    menu "gunicorn.sh"
}