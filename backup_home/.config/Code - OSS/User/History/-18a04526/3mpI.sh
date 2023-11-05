#!/bin/bash
. ./menu.sh

manage_migrations(){
    echo "MANAGING MIGRATIONS:"
    . venv/bin/activate
    cd backend
    python manage.py makemigrations
    python manage.py migrate
    deactivate
    cd ..

}

reset(){
    echo "RESETING"
    #Reseting
    delete_django
    delete_migrations_cache
    create_venv
    install_django
    create_backend
    manage_migrations
    create_superuser
}

soft_reset(){
    echo "SOFT RESET"
    delete_migrations_cache
    manage_migrations
}


delete_migrations_cache(){
    echo "DELETING MIGRATIONS AND CACHE"
    find . -type d -name "__pycache__" -exec rm -r {} +
    find . -type f -name "*00*.py" -exec rm -r {} +
    find . -type f -name "*initial*.py" -exec rm -r {} +


}


install_python3_venv(){
    echo "INSTALL PYTHON3 VENV"
    sudo apt-get install -y python3-venv
}


create_venv(){
    echo "CREATING VENV"
    python3 -m venv venv
}

install_django(){
    echo "INSTALL DJANGO"
    . venv/bin/activate
    echo "Installing pip Django"
    pip install -r requirements.txt

    deactivate
}

backup_backend(){
    mkdir -p backup/backend
    delete_migrations_cache
    cp -r backend/* backup/backend/
}

restore_backend(){
    cp -r backup/backend/* backend/
}




delete_django(){
    echo "DELETING DJANGO"
    rm -rf venv
    rm -rf backend
}


create_backend(){
    echo "CREATING BACKEND"

    . venv/bin/activate

    echo "Backend name (default:backend):"
    read backend_name
    backend=""


    if [ "$backend_name" == "" ]; then
        backend_name="backend"
    fi

    django-admin startproject $backend_name
    
    deactivate
}


create_superuser(){
    echo "CREATING SUPER USER"
    . venv/bin/activate
    cd backend
    python ./manage.py createsuperuser --noinput --email owl@owl.com --username owl --first_name owl --last_name blue --role Admin --cellphone 0000000  --password owl
    cd ..
    deactivate
}


run_test_server(){
    . venv/bin/activate
    cd backend
    python manage.py runserver
    cd ..
    deactivate
}



django_menu(){
    menu "django.sh"
}







