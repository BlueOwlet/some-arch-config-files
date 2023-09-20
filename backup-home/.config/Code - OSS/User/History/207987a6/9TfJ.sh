#!/bin/bash
. ./menu.sh

# apt-get update




# echo "deb [signed-by=/usr/share/keyrings/jitsi-keyring.gpg] https://download.jitsi.org stable/" | sudo tee /etc/apt/sources.list.d/jitsi-stable.list


# # apt-add-repository universe

# apt-get -y update

# apt-get -y install jitsi-meet



install_dependancies(){
    sudo apt purge jigasi jitsi-meet jitsi-meet-web-config jitsi-meet-prosody jitsi-meet-turnserver jitsi-meet-web jicofo jitsi-videobridge2

    sudo apt-get install -y vim wget curl 
    sudo apt-get install -y gpgv apt-transport-https nginx-full 

}

install_ubuntu_keys(){

    curl -sL https://download.jitsi.org/jitsi-key.gpg.key | sudo sh -c 'gpg --dearmor > /usr/share/keyrings/jitsi-keyring.gpg'


    # sudo wget https://download.jitsi.org/jitsi-key.gpg.key
    # sudo apt-key add jitsi-key.gpg.key
    # sudo rm jitsi-key.gpg.key

}


install_sources(){
    sudo echo "deb https://download.jitsi.org stable/" > /etc/apt/sources.list.d/jitsi-table.list
    sudo apt-get update

}


install_jitsi(){
    sudo apt install jitsi-meet

}



run_installation(){
    install_dependancies
    install_ubuntu_keys
    install_sources
    install_jitsi
}

jitsi_menu(){
    menu "jitsi.sh"
}