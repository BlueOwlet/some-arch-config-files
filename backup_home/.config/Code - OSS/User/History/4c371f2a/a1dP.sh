#!/bin/bash


download_eww(){
    git clone https://github.com/elkowar/eww


}

build_eww(){
    cd eww
    cargo build --release --no-default-features --features=wayland
    cargo build --release --no-default-features --features x11

}