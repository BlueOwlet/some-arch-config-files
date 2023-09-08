#!/bin/bash

. django.sh
. vue.sh


install_postgresql(){
    echo "Database Name: (default:project-database):"
    read database_name

    sudo apt install postgresql postgresql-contrib
    sudo apt-get install postgresql-client


sudo -u postgres psql << EOF
    DROP DATABASE IF EXISTS $database_name;
    DROP USER IF EXISTS $USER;
EOF



sudo -u postgres psql << EOF
    CREATE DATABASE $database_name;
    CREATE USER $USER WITH PASSWORD '$USER';
    ALTER ROLE $USER SET client_encoding TO 'utf8';
    ALTER ROLE $USER SET default_transaction_isolation TO 'read committed';
    ALTER ROLE $USER SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE $database_name TO $USER;
    \c $database_name postgres;
    GRANT ALL ON SCHEMA public TO $USER;


EOF


}




install_packages(){
    install_django()
    install_vue()


    install_postgresql()




}



sudo systemctl stop gunicorn

sudo systemctl stop nginx



find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*00*.py" -exec rm -r {} +
find . -type f -name "*initial*.py" -exec rm -r {} +

#rm -r venv


#sudo apt-get install redis




#pip install -r requirements






# sudo apt-get install nginx

sudo cp ./serverfiles/gunicorn.service /etc/systemd/system/gunicorn.service
sudo cp ./serverfiles/default /etc/nginx/sites-available/default




sudo systemctl start gunicorn 
sudo systemctl restart gunicorn 
# sudo systemctl enable gunicorn 

sudo systemctl restart nginx

sudo systemctl daemon-reload



#clip api stuff
    # let clip_api_key='14aae8d6-034b-4121-a330-1d850ecfa14f'
    # let clip_secret_client_key='6cdb1ccc-100d-41ea-bc9a-b2ea04a5ed32'
    # let clip_token='Basic MTRhYWU4ZDYtMDM0Yi00MTIxLWEzMzAtMWQ4NTBlY2


#github token:
    #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


