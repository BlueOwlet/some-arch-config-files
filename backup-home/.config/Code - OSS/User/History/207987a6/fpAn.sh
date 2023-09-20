#!/bin/bash
. ./menu.sh

# apt-get update



# curl -sL https://download.jitsi.org/jitsi-key.gpg.key | sudo sh -c 'gpg --dearmor > /usr/share/keyrings/jitsi-keyring.gpg'

# echo "deb [signed-by=/usr/share/keyrings/jitsi-keyring.gpg] https://download.jitsi.org stable/" | sudo tee /etc/apt/sources.list.d/jitsi-stable.list


# # apt-add-repository universe

# apt-get -y update

# apt-get -y install jitsi-meet



install_dependancies(){
    apt-get install -y vim wget curl 
    apt-get install -y gpgv apt-transport-https nginx-full 

}

install_ubuntu_keys(){
    wget https://download.jitsi.org/jitsi-key.gpg.key
    apt-key add jitsi-key.gpg.key
    rm jitsi-key.gpg.key

}


install_sources(){
    echo "deb https://download.jitsi.org stable/" >> /etc/apt/sources.list.d/jitsi-table.list
    apt-get update

}


install_jitsi(){
    apt install jitsi-meet

}


jitsi_menu(){
    install_dependancies
    install_ubuntu_keys
    install_sources
    install_jitsi
}


jitsi_menu

