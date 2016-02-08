#!/bin/bash
git clone https://github.com/lorenmanu/Tiendas.git
cd Tiendas/VagrantIV/
chmod 777 create_and_run.sh
$1 $2 $3 $4 $5 ./create_and_run.sh
