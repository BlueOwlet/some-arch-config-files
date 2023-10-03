#!/bin/bash
. ./menu.sh


install_universe_repository(){
    sudo apt-add-repository universe
    sudo apt update
}

install_dependancies(){
    sudo apt purge jigasi jitsi-meet jitsi-meet-web-config jitsi-meet-prosody jitsi-meet-turnserver jitsi-meet-web jicofo jitsi-videobridge2

    sudo apt-get install -y vim wget curl 
    sudo apt-get install -y gpgv apt-transport-https nginx-full 

}

install_ubuntu_keys(){

    curl -sL https://download.jitsi.org/jitsi-key.gpg.key | sudo sh -c 'gpg --dearmor > /usr/share/keyrings/jitsi-keyring.gpg'

    echo "deb [signed-by=/usr/share/keyrings/jitsi-keyring.gpg] https://download.jitsi.org stable/" | sudo tee /etc/apt/sources.list.d/jitsi-stable.list

    sudo apt update


}


install_sources(){
    sudo echo "deb https://download.jitsi.org stable/" > /etc/apt/sources.list.d/jitsi-table.list
    sudo apt-get update

}


install_jitsi(){
    sudo apt-get install jitsi-meet

}


install_prosody(){
    sudo curl -sL https://prosody.im/files/prosody-debian-packages.key -o /etc/apt/keyrings/prosody-debian-packages.key

    echo "deb [signed-by=/etc/apt/keyrings/prosody-debian-packages.key] http://packages.prosody.im/debian $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/prosody-debian-packages.list

    sudo apt-get install lua5.2
}

run_installation(){
    install_prosody
    install_universe_repository
    install_dependancies
    # install_ubuntu_keys
    install_sources
    install_jitsi
}



manual_installation(){
    apt-get install prosody
}

jitsi_menu(){
    menu "container.sh"
}