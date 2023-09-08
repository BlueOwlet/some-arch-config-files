#!/bin/bash



reset(){
    #Reseting
    rm -r venv
    rm -r backend


}


create_venv(){
    sudo apt-get install python3-venv
    python3 -m venv venv
    . venv/bin/activate
}


install_django(){
    pip install Django
}


create_project(){
    echo "Backend name (default:backend):"
    read=backend_name
    django-admin startproject $backend_name



}


create_superuser(){
    python ./manage.py createsuperuser --noinput --email owl@owl.com --username owl --first_name owl --last_name blue --role Admin --cellphone 0000000  --password owl
}

manage_migrations(){
    cd $backend_name
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

}



setup_django(){

    reset();
    create_venv();
    install_django();

    create_project();

    create_superuser();

    manage_migrations()



}




