#!/bin/bash

# Install Node.js and npm
sudo apt update
sudo apt install -y nodejs npm

# Install Vue CLI
npm install -g @vue/cli

# Create a new Vue 3 project named "frontend"
vue create frontend

# Navigate to the project directory
cd vyda-frontend

# Start the development server
npm run serve
