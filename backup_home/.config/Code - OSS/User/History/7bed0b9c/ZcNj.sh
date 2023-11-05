#!/bin/bash

. menu.sh

local_backup(){
    echo "CREATING LOCAL BACKUP"
    mkdir -p ~/Desktop/local_backup
    cp -r * ~/Desktop/local_backup/
    echo "LOCAL BACKUP CREATED IN DESKTOP"
}


restore_backup_to_server(){
    cp -r ~/Desktop/local_backup/* ~/vyda/
}


backup_menu(){
    menu "backup.sh"
}