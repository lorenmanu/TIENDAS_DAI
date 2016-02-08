#!/bin/bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo docker pull lorenmanu/Tiendas
sudo docker run -t -i lorenmanu/Tiendas /bin/bash
