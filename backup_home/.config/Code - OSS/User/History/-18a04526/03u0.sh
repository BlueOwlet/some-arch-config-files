#!/bin/bash


delete_migrations_cache(){
    echo "DELETING MIGRATIONS AND CACHE"
    find . -type d -name "__pycache__" -exec rm -r {} +
    find . -type f -name "*00*.py" -exec rm -r {} +
    find . -type f -name "*initial*.py" -exec rm -r {} +


}

reset(){
    echo "RESETING"
    #Reseting
    delete_django
    delete_migrations_cache
    create_venv
    install_django
    manage_migrations
}

soft_reset(){
    echo "SOFT RESET"
    delete_migrations_cache
    manage_migrations
}

install_python3_venv(){
    echo "INSTALL PYTHON3 VENV"
    sudo apt-get install python3-venv
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

    if [ "$backend_name" == "" ]; then
        backend_name="backend"
    fi

    django-admin startproject $backend_name
    
    deactivate
}


create_superuser(){
    echo "CREATING SUPER USER"

    cd backend
    python ./manage.py createsuperuser --noinput --email owl@owl.com --username owl --first_name owl --last_name blue --role Admin --cellphone 0000000  --password owl
    cd ..
}

manage_migrations(){
    echo "MANAGING MIGRATIONS:"
    . venv/bin/activate
    cd backend
    python manage.py makemigrations
    python manage.py migrate
    deactivate
    cd ..

}


list_functions(){

    # echo "LISTING FUNCTION:"
    awk_output=`awk -F '\(' '/\(){/ {print $1}' django.sh`    
    readarray -t funcs <<< "$awk_output"
    counter=0
    for func in $funcs
    do
        echo "this is counter: $counter"
        ((counter++))
        echo "$counter $func"
    done
    echo "Select Option:"
}

select_option(){
    local option
    read option
}



django_menu() {

    while true
    do
        
        list_functions
        local option=`select_option`


        echo "RUNNING FUNCTION: $option"

        ${funcs[0]}
        case $option in
            1)
                install_python3_venv
                ;;
            2)
                create_venv
                ;;
            3)
                install_django
                ;;
            4)
                create_backend
                ;;
            5)
                create_superuser
                ;;
            6)
                manage_migrations
                ;;
            7)
                reset
                ;;
            8)
                soft_reset
                ;;



            "")
                echo "Returning to previous menu"
                break
                ;;
            *)
                echo "option not valid"
                ;;
        esac
    done



}





