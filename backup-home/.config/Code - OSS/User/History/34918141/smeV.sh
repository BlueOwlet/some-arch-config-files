#!/bin/bash

apt-get update
apt-get install -y vim wget curl 
apt-get install -y gpgv apt-transport-https nginx-full 


echo 'deb [signed-by=/usr/share/keyrings/jitsi-keyring.gpg] https://download.jitsi.org stable/' | tee /etc/apt/sources.list.d/jitsi-stable.list > /dev/null

wget https://download.jitsi.org/jitsi-key.gpg.key |  sh -c 'gpg --dearmor > /usr/share/keyrings/jitsi-keyring.gpg'
apt-add-repository universe

apt-get -y update

 apt-get -y install jitsi-meet



# apt-get install -y jitsi-meet