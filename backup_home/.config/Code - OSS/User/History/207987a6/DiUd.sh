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


run_installation(){
    install_tools
    jitsi_gpc_key
    prosody_gpc_key
    install_jitsi
}

jitsi_docker_download(){
    cd ~
    rm -r *jitsi*
    rm stable*
    wget https://github.com/jitsi/docker-jitsi-meet/archive/refs/tags/stable-8960-1.tar.gz
    tar -zxvf *.tar*
    mv docker* jitsi
    cdw
    pwd
}

jitsi_docker_installation(){

    
    cp jitsi.env.bak ~/jitsi/.env    
    cd ~/jitsi
    ./gen-passwords.sh
    mkdir -p ~/.jitsi-meet-cfg/{web,transcripts,prosody/config,prosody/prosody-plugins-custom,jicofo,jvb,jigasi,jibri}
    cdw

    # sudo apt install containernetworking-plugins
    # sudo apt update
    # podman system reset --force

}

jitsi_podman_compose(){
    cd ~/jitsi

    podman-compose up
    cdw
}


jitsi_menu(){
    menu "jitsi.sh"
}