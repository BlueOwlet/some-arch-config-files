#!/bin/bash
. menu.sh

compiler_patch(){
    echo "INSTALLING sfc-compiler PATCH"
    #in case of sfc-copmpiler error
    npm i vue@3.2.26
}


install_vue(){
    echo "INSTALLING VUE"
    #these were with  before, don't know why, though.
     npm install -g @vue/cli
     npm update -g @vue/cli
     npm install axios
    compiler_patch

    npm audit fix --force
}


first_install_vue(){
    echo "INSTALL NODE, NPM AND VUE"
     apt update
     apt-get install nodejs
     apt-get install npm
    install_vue
}



uninstall_vue_full(){
    echo "FULLY UNINSTALLING"
    #Uninstall node.js and npm and 
    rm -rf frontend/

     npm uninstall -g @vue/cli
     npm clear cache --force

     npm uninstall npm -g
     rm -rf /usr/local/{lib/node{,/.npm,_modules},bin,share/man}/npm*
     rm /user/bin/node
     apt-get remove nodejs
     apt-get purge nodejs
     apt-get purge – auto-remove nodejs
     apt-get autoremove



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


build_vue_project(){
    echo "REBUILDING"
    cd frontend
    npm run build
    cd ..
}


vue_menu(){
    menu "vue.sh"

}