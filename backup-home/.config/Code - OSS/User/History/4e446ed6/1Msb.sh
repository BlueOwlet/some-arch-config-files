#!/bin/bash
list_functions(){

    
    local file=$1
    echo "MENU FOR: $file"
    awk_output=`awk -F '\(' '/\()\{/ {print $1}' $file`    

    readarray -t funcs <<< "$awk_output"
    counter=0
    for func in ${funcs[@]}
    do
        ((counter++))
        echo "$counter $func"
    done
    echo "Select Option (default: exit):"
}

select_option(){
    local option
    read option
    echo $option
}



menu() {

    local file=$1

    while true
    do
        
        list_functions $file
        local option=`select_option`
        

        echo "RUNNING FUNCTION: $option"
        if [ $option == "" ];then
            break
        fi
        ${funcs[$option-1]}
    done



}
