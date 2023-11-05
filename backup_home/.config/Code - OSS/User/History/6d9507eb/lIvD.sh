#!/bin/bash
. menu.sh

compiler_patch(){
    echo "INSTALLING sfc-compiler PATCH"
    #in case of sfc-copmpiler error
    npm i vue@3.2.26
}


install_vue(){
    echo "INSTALLING VUE"
    #these were with sudo before, don't know why, though.
    sudo npm install -g @vue/cli
    sudo npm update -g @vue/cli
    sudo npm install axios

    npm audit fix --force
}


first_install_vue(){
    echo "INSTALL NODE, NPM AND VUE"
    sudo apt update
    sudo apt-get install -y nodejs
    sudo apt-get install -y npm
    install_vue
}



uninstall_vue_full(){
    echo "FULLY UNINSTALLING"
    #Uninstall node.js and npm and 
    rm -rf frontend/

    sudo npm uninstall -g @vue/cli
    sudo npm clear cache --force

    sudo npm uninstall npm -g
    sudo rm -rf /usr/local/{lib/node{,/.npm,_modules},bin,share/man}/npm*
    sudo rm /user/bin/node
    sudo apt-get remove nodejs
    sudo apt-get purge nodejs
    sudo apt-get purge – auto-remove nodejs
    sudo apt-get autoremove



}

reinstall_vue(){
    echo "REINSTALLING VUE COMPLETELY"
    echo "backup src folder?"
    read backup
    if [ "$backup" = "y" ];then
        backup_vue_project
    fi
    uninstall_vue_full
    first_install_vue
}



create_frontend(){
    echo "CREATING FRONTEND"
    vue create -f frontend
    cd frontend
    compiler_patch

    npm run build

}


backup_vue_project(){
    echo "BACKING UP VUE"
    mkdir -p backup/frontend
    cp -r frontend/src/ backup/frontend/ 

}


restore_vue_project(){
    echo "RESTORING VUE BACKUP"
    cp -r backup/frontend/src/ frontend/ 
}


rebuild_vue_project(){
    echo "REBUILDING"
    cd frontend
    npm run build
    cd ..
}


vue_menu(){
    menu "vue.sh"

}