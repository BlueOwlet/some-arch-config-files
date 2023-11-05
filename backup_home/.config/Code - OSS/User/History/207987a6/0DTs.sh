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
    sudo rm -r *jitsi*
    sudo rm stable*
    wget https://github.com/jitsi/docker-jitsi-meet/archive/refs/tags/stable-8960-1.tar.gz
    tar -zxvf *.tar*
    mv docker* jitsi
    cdw
    pwd
}



jitsi_docker_installation(){

    # cp backup/jitsi/jitsi.env.bak ~/jitsi/.env
    cp backup/jitsi/env.example ~/jitsi/.env
    
    cd ~/jitsi
    chmod +x gen-passwords.sh
    ./gen-passwords.sh
    mkdir -pv ~/.jitsi-meet-cfg/{web,transcripts,prosody/config,prosody/prosody-plugins-custom,jicofo,jvb,jigasi,jibri}
    cdw



}


jitsi_podman_compose(){
    cd ~/jitsi

    # podman-compose up -d 
    docker-compose up -d
    cdw
}

backup_jitsi(){
    mkdir -p backup/jitsi/
    sudo cp ~/.config/cni/net.d/jitsi_meet.jitsi.conflist backup/jitsi
    sudo cp ~/jitsi/docker-compose.yml backup/jitsi
    sudo cp ~/jitsi/.env backup/jitsi

}

restore_jitsi(){

    # sudo rm /etc/cni/net.d/*jitsi*
    # sudo rm ~/.config/cni/net.d/*jitsi*
    # sudo cp backup/jitsi/jitsi_meet.jitsi.conflist /etc/cni/net.d/
    # sudo cp backup/jitsi/jitsi_meet.jitsi.conflist ~/.config/cni/net.d/
    # sudo systemctl restart docker

    sudo cp backup/jitsi ~/jitsi/docker-compose.yml


}



refresh_jitsi(){
    sudo rm -r ~/.jitsi-meet-cfg
}


run_all(){
    refresh_jitsi
    jitsi_docker_download
    jitsi_docker_installation
    restore_jitsi
    veth_driver
    jitsi_podman_compose
}


jitsi_menu(){
    menu "jitsi.sh"
}