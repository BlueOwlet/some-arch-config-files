#!/bin/bash

apt-get update
apt-get install -y gpgv nginx-full wget
apt-get install -y apt-transport-https

apt-add-repository universe

# apt update
apt-get update

apt-get install -y jitsi-meet