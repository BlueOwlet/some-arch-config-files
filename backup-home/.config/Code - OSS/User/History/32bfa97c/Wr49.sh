#!/bin/bash
. ./menu.sh



install_postgresql(){
    echo "Database Name: (default:backend_database):"
    read database_name
    database_name="backend_database"

    sudo apt install postgresql postgresql-contrib
    sudo apt-get install postgresql-client

}

delete_database(){

sudo -u postgres psql << EOF
    DROP DATABASE IF EXISTS backend_database;
    DROP USER IF EXISTS $user;
EOF

}




create_database(){

sudo -u postgres psql << EOF
    CREATE DATABASE backend_database;
    CREATE USER $user WITH PASSWORD '$user';
    ALTER ROLE $user SET client_encoding TO 'utf8';
    ALTER ROLE $user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE $user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE backend_database TO $user;
    \c backend_database postgres;
    GRANT ALL ON SCHEMA public TO $user;


EOF





}


user=$USER

postgres_menu(){

    menu "postgres.sh"
}
