#!/bin/bash

apt-get update
apt-get install -y vim wget curl
apt-get install -y gpgv apt-transport-https nginx-full 

wget https://download.jitsi.org/jitsi-key.gpg.key | sudo sh -c 'gpg --dearmor > /usr/share/keyrings/jitsi-keyring.gpg'

apt-add-repository universe

apt-get update

# apt-get install -y jitsi-meet