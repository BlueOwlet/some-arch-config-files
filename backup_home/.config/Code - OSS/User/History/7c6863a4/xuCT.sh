#!/bin/bash
. ./menu.sh


install_gunicorn(){
    sudo apt-get install gunicorn
    sudo systemctl stop gunicorn
    sudo cp backup/gunicorn.service /etc/systemd/system/gunicorn.service
    sudo systemctl start gunicorn 

}



gunicorn_menu(){
    menu "gunicorn.sh"
}