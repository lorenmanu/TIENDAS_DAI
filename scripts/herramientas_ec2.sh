echo " Instalación pip si no está instalado"
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python27 get-pip.py
echo "Instalación virtual-box"
deb http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib | sudo tee /etc/apt/sources.list.d/virtualbox.list
wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- | sudo apt-key add -
sudo apt-get update
sudo apt-get install virtualbox-4.0
echo "Instalación vagrant"
sudo wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
sudo dpkg -i vagrant_1.8.1_x86_64.deb
echo " Instalación COMMAND LINE INTERFACE DE EC2"
sudo pip install awscli
echo " Instalación de ansible para el despligue remoto en PAAS "
sudo pip install paramiko PyYAML jinja2 httplib2 ansible
echo "Instalación de plugin de vagrant aws para el despliegue remoto en PAAS"
vagrant plugin install aws
