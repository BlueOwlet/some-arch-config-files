#!/bin/bash

. ./menu.sh






install_tools(){
    sudo apt-get install curl gnupg2 wget -y


}




jitsi_gpc_key(){
    curl https://download.jitsi.org/jitsi-key.gpg.key -o jitsi-key.gpg.key
    gpg --output /usr/share/keyrings/jitsi-key.gpg --dearmor jitsi-key.gpg.key
    echo "deb [signed-by=/usr/share/keyrings/jitsi-key.gpg] https://download.jitsi.org stable/" > /etc/apt/sources.list.d/jitsi-stable.list

}

prosody_gpc_key(){
    curl https://prosody.im/files/prosody-debian-packages.key -o prosody-debian-packages.key
    gpg --output /usr/share/keyrings/prosody-keyring.gpg --dearmor prosody-debian-packages.key
    echo "deb [signed-by=/usr/share/keyrings/prosody-keyring.gpg] http://packages.prosody.im/debian jammy main" > /etc/apt/sources.list.d/prosody.list
}


install_jitsi(){
    sudo apt-get update -y
    sudo apt-get install jitsi-meet -y
}

full_jitsi_uninstall(){
    sudo apt purge jigasi jitsi-meet jitsi-meet-web-config jitsi-meet-prosody jitsi-meet-turnserver jitsi-meet-web jicofo jitsi-videobridge2
    rm /etc/apt/sources.list.d/jitsi-stable.list
    rm /etc/apt/sources.list.d/prosody.list
}


run_jitsi_installation(){
    install_tools
    jitsi_gpc_key
    prosody_gpc_key
    install_jitsi
}




rund_docker_installation(){
    wget https://github.com/jitsi/docker-jitsi-meet/archive/refs/tags/stable-8922-1.tar.gz
    tar -xvf stable*.tar.gz
    rm *.tar.gz
    cd docker*
    cp env.example .env
    

}



jitsi_menu(){
    menu "jitsi.sh"
}