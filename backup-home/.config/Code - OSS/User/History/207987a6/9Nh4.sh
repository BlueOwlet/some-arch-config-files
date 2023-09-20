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





run_installation(){
}



jitsi_menu(){
    menu "jitsi.sh"
}