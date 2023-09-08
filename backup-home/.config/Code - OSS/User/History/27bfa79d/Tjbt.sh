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
}

setup_django(){

    reset();
    create_venv();
    install_django();

    create_project();



}








# Create a Django project

# Navigate to the project directory
cd backend

# Create a Django app (optional)
# python manage.py startapp your_app_name

# Run migrations (create the initial database schema)
python manage.py makemigrations
python manage.py migrate

# Create a superuser (admin) account (optional)
# python manage.py createsuperuser

# Start the development server
python manage.py runserver
