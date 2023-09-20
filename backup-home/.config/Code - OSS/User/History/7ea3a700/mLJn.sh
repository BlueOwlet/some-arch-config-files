. ./menu.sh


install_podman(){
    sudo apt-get install -y podman

}

download_base_image(){
    podman pull docker.io/library/ubuntu

}

create_container(){



    echo "Make Ethereal (default y)"
    read ethereal

    if [ $ethereal = "" ];then

        podman run --rm -ti -p 80:80 -p 10000:10000  -v /var/www/vyda-project:/home/ --name jitsi-meet ubuntu
    else
        podman run -ti -p 5000:80 -p 10000:10000 -v /var/www/vyda-project:/home/ --name jitsi-meet ubuntu
    
    fi
    
    
    
    
    


}

rerun_container(){
    podman run jitsi-meet
    podman restart jitsi-meet
    podman exec -ti jitsi-meet /bin/bash

}

first_run(){
    install_podman
    download_base_image
    create_container
}

reset_podman(){
    podman stop -a
    podman image rm -a
    podman container rm -a
    podman rm -a

    podman images
    podman ps -a
}

podman_menu(){
    menu "podman.sh"
}