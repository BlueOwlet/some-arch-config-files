#!/bin/bash
. ./menu.sh



install_postgresql(){
    echo "Database Name: (default:project-database):"
    read database_name

    sudo apt install postgresql postgresql-contrib
    sudo apt-get install postgresql-client

}

delete_database(){
sudo -u postgres psql << EOF
    DROP DATABASE IF EXISTS $database_name;
    DROP USER IF EXISTS $USER;
EOF

}




create_database(){

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

postgres_menu(){
    menu "postgres.sh"
}
