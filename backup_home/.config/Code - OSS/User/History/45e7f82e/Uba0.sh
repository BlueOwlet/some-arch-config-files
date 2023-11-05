#!/bin/bash

. menu.sh




install_prerequisites(){
    sudo apt install snapd
}

install_certbot(){
    sudo snap install --classic certbot
    sudo ln -s /snap/bin/certbot /usr/bin/certbot
}



refresh_certbot(){
    sudo certbot delete
    # sudo certbot delete --cert-name vyda.mx
    # sudo certbot delete --cert-name *.vyda.mx

}

remove_cerbot(){
    refresh_certbot
    sudo snap remove certbot
    sudo rm /usr/bin/certbot
}

run_certbot(){

    echo """CHOOSE DOMAINS

        1.- vyda.mx
        2.- *vyda.mx
        3.- all
    
    
    """
    read option


    case $option in
        1)
            sudo certbot --nginx -v --agree-tos --preferred-challenges=dns -d vyda.mx
            ;;
        2)
            sudo certbot certonly --nginx -v --agree-tos --preferred-challenges=dns -d *.vyda.mx
            ;;



    # sudo systemctl restart nginx
    # sudo certbot --preferred-challenges=dns -d vyda.mx,*.vyda.mx --nginx
    sudo systemctl restart nginx

}


certbot_menu(){
    menu "certbot.sh"
}