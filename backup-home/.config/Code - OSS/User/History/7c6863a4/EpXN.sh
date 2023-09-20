#!/bin/bash
. ./menu.sh


install_gunicorn(){
    sudo apt-get install gunicorn

}

restore_gunicorn_to_project_folder(){
    mkdir -p gunicorn
    sudo cp backup/gunicorn/gunicorn.service gunicorn/
    sudo cp backup/gunicorn/gunicorn-config.py gunicorn/

}

reload_gunicorn(){
    sudo cp backup/gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
    sudo systemctl start gunicorn 
}

restart_gunicorn(){
    sudo systemctl restart gunicorn
}



gunicorn_menu(){
    menu "gunicorn.sh"
}