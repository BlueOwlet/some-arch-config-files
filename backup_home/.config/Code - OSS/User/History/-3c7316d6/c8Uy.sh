#!/bin/bash
. ./menu.sh


install_gunicorn(){
     apt-get install gunicorn

}

restore_gunicorn_to_project_folder(){
    mkdir -p gunicorn
     cp backup/gunicorn/gunicorn.service gunicorn/
     cp backup/gunicorn/gunicorn-config.py gunicorn/

}

reload_gunicorn(){
     cp gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
     systemctl start gunicorn 
     systemctl reload gunicorn
     systemctl restart gunicorn
     systemctl daemon-reload
}

backup_gunicorn(){
    mkdir -p backup/gunicorn
     cp /etc/systemd/system/gunicorn.service backup/gunicorn/
     cp gunicorn/gunicorn-config.py backup/gunicorn/
}


gunicorn_menu(){
    menu "gunicorn.sh"
}