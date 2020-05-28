#!/bin/bash

# Copy files to server
scp -r ./* root@45.79.103.179:/home/root

# SSH to server
# Switch to directory
# Run docker command
ssh root@45.79.103.179 "cd /home/root && docker-compose up --build -d"

# Exit server
# exit