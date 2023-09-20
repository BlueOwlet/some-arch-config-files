#!/bin/bash
. menu.sh

compiler_patch(){
    #in case of sfc-copmpiler error
    npm i vue@3.2.26
}


install_vue(){
    sudo npm install -g @vue/cli
    sudo npm update -g @vue/cli
    compiler_patch

    npm audit fix --force
}


first_install_vue(){
    sudo apt update
    sudo apt-get install nodejs
    sudo apt-get install npm
    install_vue
}



uninstall_vue_full(){
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

    echo "backup src folder?"
    read backup
    if [ $backup = "y" ];then
        backup_vue_project
    fi
    uninstall_vue_full
    install_vue
}



create_frontend(){
    vue create -f frontend
    cd frontend
    npm run build

}


backup_vue_project(){
    mkdir -p vue-backup
    cp -r frontend/src/ vue-backup/

}


restore_vue_project(){
    cp -r vue-backup/src/ frontend/ 
}


rebuild_vue_project(){
    cd frontend
    npm run build
}


vue_menu(){
    menu "vue.sh"

}