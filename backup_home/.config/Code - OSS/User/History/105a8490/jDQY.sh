#!/bin/bash
. django.sh
. vue.sh
. postgres.sh

install_nginx(){

    sudo apt-get install nginx
    sudo systemctl start nginx
    sudo systemctl enable nginx

}

install_gunicorn(){
    sudo apt-get install gunicorn
    sudo systemctl stop gunicorn
    sudo cp backup/gunicorn.service /etc/systemd/system/gunicorn.service
    sudo systemctl start gunicorn 

}




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




main(){



    while true
    do

        echo "f: First Run | r: Reset | s: SoftReset | v: Vue Menu | d: Django Menu | p: Postgres Menu | g: Gunicorn Menu"

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
