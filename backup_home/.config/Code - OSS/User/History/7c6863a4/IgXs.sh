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
    sudo cp gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
    sudo systemctl start gunicorn 
    sudo systemctl restart gunicorn
    sudo systemctl daemon-reload
}

backup_gunicorn(){
    mkdir -p backup/gunicorn
    sudo cp /etc/systemd/system/gunicorn.service backup/gunicorn/
    sudo cp gunicorn/gunicorn-config.py backup/gunicorn/
}


gunicorn_menu(){
    menu "gunicorn.sh"
}