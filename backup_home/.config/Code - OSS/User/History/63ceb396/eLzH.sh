#!/bin/bash
. django.sh
. vue.sh
. postgres.sh
. nginx.sh
. gunicorn.sh




master_reset(){
    sudo systemctl restart gunicorn 
    # sudo systemctl enable gunicorn 

    sudo systemctl restart nginx

    sudo systemctl daemon-reload
}


#clip api stuff
    # let clip_api_key='14aae8d6-034b-4121-a330-1d850ecfa14f'
    # let clip_secret_client_key='6cdb1ccc-100d-41ea-bc9a-b2ea04a5ed32'
    # let clip_token='Basic MTRhYWU4ZDYtMDM0Yi00MTIxLWEzMzAtMWQ4NTBlY2


#github token:
    #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




container_install(){
    
    #VUE
    first_install_vue
    create_frontend
    restore_vue_project
    build_vue_project
    #DJANGO
    install_python3_venv
    create_venv
    install_django
    create_backend
    create_superuser
    manage_migrations
    #GUNICORN   
    install_gunicorn
    restore_gunicorn_to_project_folder
    reload_gunicorn
    #NGINX
    install_and_enable_nginx
    restore_nginx_sites_available
    reload_nginx



}


main(){

    container=$1

    if [ $container = "container" ];then
        container_install
    fi

    while true
    do

        echo "f: First Run | r: Reset | s: SoftReset | v: Vue Menu | d: Django Menu | p: Postgres Menu | g: Gunicorn Menu | n: Nginx"

        read option
        
        case $option in

            "v")
                vue_menu
                ;;
            "d")
                django_menu
                ;;
            "p")
                postgres_menu
                ;;
            "n")
                nginx_menu
                ;;
            "g")
                gunicorn_menu
                ;;
            "")
                echo "Exiting"
                break
        esac
    done

}

main
