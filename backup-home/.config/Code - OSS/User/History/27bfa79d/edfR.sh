#!/bin/bash


reset(){
    #Reseting
    rm -r venv
    rm -r backend
    find . -type d -name "__pycache__" -exec rm -r {} +
    find . -type f -name "*00*.py" -exec rm -r {} +
    find . -type f -name "*initial*.py" -exec rm -r {} +
}

soft_reset(){
    find . -type d -name "__pycache__" -exec rm -r {} +
    find . -type f -name "*00*.py" -exec rm -r {} +
    find . -type f -name "*initial*.py" -exec rm -r {} +
}


create_venv(){
    sudo apt-get install python3-venv
    python3 -m venv venv
}


install_django(){
    . venv/bin/activate
    echo "Installing pip Django"
    pip install Django
}


create_backend(){
    echo "Backend name (default:backend):"
    read backend_name
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

    reset()
    

    install_django()

    create_backend()

    create_superuser()

    manage_migrations()



}




