#!/bin/bash

. menu.sh

local_backup(){
    mkdir -p ~/Desktop/
    cp * ~/Desktop/
}



backup_menu(){
    menu "backup.sh"
}