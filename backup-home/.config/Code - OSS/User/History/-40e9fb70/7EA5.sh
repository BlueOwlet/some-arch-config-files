#!/bin/bash

. ./menu.sh


install_basic_programs(){
	apt-get update 
	apt-get install -y sudo vim htop wget curl

}


copy_all(){

	rm -r /home/owl/Desktop/container/*
	rsync --progress -r ./* ~/Desktop/container/

}


copy_manage(){

	rsync --progress ./*.sh ~/Desktop/container/
}

container_menu(){

	menu "container.sh"

}


main
