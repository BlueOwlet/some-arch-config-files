#!/bin/bash

. django.sh
. vue.sh
. postgres.sh





install_packages(){
    echo "Install Django?"
    read install
    if ($install="y");then
        install_django();
    fi

    echo "Install Vue?"
    read install
    if ($install="y");then
        install_vue();
    fi
    echo "Install Postgres?"
    read install
    if ($install="y");then
        install_postgresql();
    fi
    echo "Install Nginx?"
    read install
    if ($install="y");then
        install_nginx();
    fi





}






install_nginx(){

    sudo apt-get install nginx
    sudo systemctl start nginx
    sudo systemctl enable nginx

}

install_gunicorn(){
    sudo systemctl stop gunicorn
    sudo cp ./serverfiles/gunicorn.service /etc/systemd/system/gunicorn.service
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
    install_packages()
}




main()
