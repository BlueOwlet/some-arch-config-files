#!/bin/bash



reset(){
    #Reseting
    rm -r venv
    rm -r backend


}


create_venv(){
    # Create a virtual environment (optional but recommended)
    python3 -m venv venv
    source venv/bin/activate
}


install_django(){
    # Install Django
    pip install Django


}


create_project(){
    echo "Backend name (default:backend):"
    read=backend_name
    django-admin startproject $backend_name


    cd $backend_name
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

}

manage_migrations(){

}

setup_django(){

    reset();
    create_venv();
    install_django();

    create_project();

    manage_migrations()



}








# Create a Django project

