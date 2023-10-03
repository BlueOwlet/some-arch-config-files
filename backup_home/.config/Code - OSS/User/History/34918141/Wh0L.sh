#!/bin/bash

apt-get update
apt-get install gpgv nginx-full wget
apt install apt-transport-https

apt-add-repository universe

apt update