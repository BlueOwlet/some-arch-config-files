#!/bin/bash


install_starship(){
    touch ~/.config/starship.toml
    curl -sS https://starship.rs/install.sh | sh
}