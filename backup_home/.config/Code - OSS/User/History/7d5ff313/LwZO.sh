#!/bin/bash

. menu.sh

local_backup(){
    echo "CREATING LOCAL BACKUP"
    mkdir -p ~/Desktop/
    cp * ~/Desktop/
    echo "LOCAL BACKUP CREATED"
}



backup_menu(){
    menu "backup.sh"
}