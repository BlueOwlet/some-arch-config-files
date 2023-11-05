#!/bin/bash

. menu.sh




install_prerequisites(){
    sudo apt install snapd
}

backup_certificates(){
    mkdir -p backup/certbot
    sudo cp -r /etc/letsencrypt/live backup/certbot/
}

restore_certificates(){
    sudo cp -r backup/certbot/live /etc/letsencrypt/

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
    sudo snap remove --purge certbot
    sudo rm /usr/bin/certbot
}

run_certbot(){

    echo """CHOOSE DOMAINS
        REQUEST NEW CERT OPTIONS:
        1.- vyda.mx
        2.- *.vyda.mx
        3.- all

        USE PREVIOUS CERT OPTIONS
        4.- only do install portion, this uses previously requested certificates

        5.- certonly --manual
    
    
    """
    read option


    case $option in
        1)
            sudo certbot --nginx -v --agree-tos --preferred-challenges=dns -d vyda.mx
            ;;
        2)
            sudo certbot certonly --nginx -v --agree-tos --preferred-challenges=dns -d *.vyda.mx
            ;;
        3)
            sudo certbot --nginx -v --agree-tos --preferred-challenges=dns -d vyda.mx -d *.vyda.mx
            # sudo certbot certonly --nginx -v --agree-tos --preferred-challenges=dns -d *.vyda.mx
            ;;
        4)
            sudo certbot --nginx --cert-name vyda.mx -d vyda.mx -d *.vyda.mx
            ;;
        5)
            sudo certbot certonly --manual --preferred-challenges=dns -v -d vyda.mx -d *.vyda.mx
            ;;

    esac


    # sudo systemctl restart nginx
    # sudo certbot --preferred-challenges=dns -d vyda.mx,*.vyda.mx --nginx
    sudo systemctl restart nginx

}


certbot_menu(){
    menu "certbot.sh"
}