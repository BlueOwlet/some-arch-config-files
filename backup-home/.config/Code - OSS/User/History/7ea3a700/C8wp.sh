install_podman(){
    apt-get install -y podman

}

download_base_image(){
    podman pull docker.io/library/ubuntu

}

create_container(){
    podman run -ti -p 8001:80 -p 10000:10000 --rm -v /var/www/vyda-project:/home/ --name jitsi-container
}