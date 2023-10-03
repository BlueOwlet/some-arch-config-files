#!/bin/bash


download_eww(){
    git clone https://github.com/elkowar/eww


}

build_eww(){
    cd eww
    if [ $XDG_SESSION_TYPE = 'wayland' ];then
        echo "RUNNING ON WAYLAND"
        cargo build --release --no-default-features --features=wayland
    elif [ $XDG_SESSION_TYPE = 'wayland' ];then
        echo "RUNNING ON X11"
        cargo build --release --no-default-features --features x11
    else 
        echo "UNKNOWN XDG SESSION TYPE"
    fi
}