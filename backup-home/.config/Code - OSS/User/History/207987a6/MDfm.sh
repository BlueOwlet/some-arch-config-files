#!/bin/bash

. ./menu.sh






install_tools(){
    sudo apt-get install curl gnupg2 wget -y


}


gpc_key(){
    curl https://download.jitsi.org/jitsi-key.gpg.key -o jitsi-key.gpg.key
    gpg --output /usr/share/keyrings/jitsi-key.gpg --dearmor jitsi-key.gpg.key
    echo "deb [signed-by=/usr/share/keyrings/jitsi-key.gpg] https://download.jitsi.org stable/" > /etc/apt/sources.list.d/jitsi-stable.list
    
}





run_installation(){
}



jitsi_menu(){
    menu "jitsi.sh"
}