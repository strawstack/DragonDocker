#!/bin/bash

# Copy files to server
scp -r ./* root@$1:/home/root

# SSH to server
# Switch to directory
# Run docker command
ssh root@$1 "cd /home/root && docker-compose up --build -d"

# Exit server
# exit