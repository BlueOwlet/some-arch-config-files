#!/bin/bash
. menu.sh

install_starship(){
    touch ~/.config/starship.toml
    curl -sS https://starship.rs/install.sh | sh

}



starship_menu(){
    menu "starship.sh"
}