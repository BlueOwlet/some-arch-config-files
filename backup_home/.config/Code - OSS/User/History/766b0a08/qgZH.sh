#!/bin/bash





install_vue(){

    sudo apt update



    sudo apt-get install nodejs
    sudo apt-get install npm
    sudo npm install -g @vue/cli
    # sudo npm install vuex
    # npm install vue-router
    # npm audit fix --force

}

uninstall_vue_full(){
    #Uninstall node.js and npm and vue
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




# Install Node.js and npm

# Install Vue CLI
sudo npm install -g @vue/cli
sudo npm update -g @vue/cli

npm i vue@3.2.26

# Create a new Vue 3 project named "frontend"
vue create -f frontend

# Navigate to the project directory
cd frontend

# Start the development server
npm run serve
