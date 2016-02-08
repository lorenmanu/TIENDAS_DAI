### Explicación del proceso del despliegue de la aplicación en IAAS EC2 usando VAGRANT y ANSIBLE

---------
### Instalación de herramientas
---------

Antes de nada se debera instalar las herramientas necesarias para poder trabajar, se ha proporcionado un archivo que permite realizarlo. Se ubica en la carpeta **scrtips** del repositorio, concretamente se puede ver [aqui](https://github.com/lorenmanu/Tiendas/blob/master/scripts/herramientas_ec2.sh). Lo que hace se puede ver en el propio archivo, para ello se lanza mensajes explicativos mediante  **echo**.


---------
### Configuración de COMMAND LINE INTERFACE (CLI)
----------
Para poder tener **COMMAND LINE INTERFACE** en nuestro ordenador para realizar tareas de administración de nuestro perfil( creación de **Security Groups**, **archivos .pem** para conexción ssh con nuestra instancia...) deberemos seguir los siguientes pasos:

- Instalar el cliente de **Command Line Interface** de Amazon, el cual me permitirá realizar tareas de gestión de mi perfil de usuario. Se puede consultar la documentación oficial, concretamente en el [apartado](http://docs.aws.amazon.com/es_es/cli/latest/userguide/installing.html).

- Una vez instalado en nuestro ordenador, procederemos a configurarlo, para ello debemos poner en la terminal:

```
aws configure

```

Este comando nos pedirá que rellenemos una serie de primitivas, la cual permitirán a **Command Line Interface** conectarse a nuestro perfil de Amazon. No se muestra pantallazo, debido a razones de seguridad.


De la siguiente imagen, pasamos a mostrar como rellenar los campos que nos piden el anterior comando:

- Nos dirigimos a nuestro perfil de Amazon( lo que viene siendo loguearse como en cualquier plataforma). Una vez dentro seleccionamos nuestro nombre de perfil y le damos al apartado **Security Credentials**.

![img15](https://www.dropbox.com/s/gygkl6oneu1hwrg/img15.png?dl=1)

- Una vez dentro, nos vamos al apartado **Users**:

![img16](https://www.dropbox.com/s/8y7vo3cddw4iluw/img16.png?dl=1)

- Le damos a la pestaña **Create New User**:

![img17](https://www.dropbox.com/s/jc09db3cn307ggn/img17.png?dl=1)

- Una vez dado nos pedirá que rellenemos una seria de campos:

![img18](https://www.dropbox.com/s/tao3m85ray0x8as/img18.png?dl=1)

- Cuando pinchamos en crear, se nos descargará un archivo **.csv**, deberemos guardarlo ya que contiene los campos necesarios para **aws configure**, ahora lo veremos.

- Si todos los pasos anteriores se ha realizado correctamente debe salirnos ya el usuario, en mi caso yo he creado un usuario denominado **lorenmanu**:

![img19](https://www.dropbox.com/s/r4mjdiqro8jxx7g/img19.png?dl=1)

- Tenemos que darle los permisos necesarios al usuario para que pueda trabajar con nuestro perfil, esto lo haremos en el apartado **Permissions**. Dentro de este apartado se deberá dar a **Attach Policy** para darle permisos. Se nos ofrece una gran variedad de permisos que le podemos dar al usuario, en mi caso he optado por **AmazonEC2FullAccess**, ya que es que me permite trabajar en versión gratuita:

![img20](https://www.dropbox.com/s/bgyoifrn3skbli7/img20.png?dl=1)


- Recuperamos el archivos **.csv**, lo abrimos, y de ahí cogeremos los campos:

```
access_key_id

secret_access_key

```

- Ya podemos volver a usar **aws configure**, y rellenar los campos necesarios. Los dos campos del paso anterior son los importantes, en los otros dos que se nos pedirán rellenar:

 - **region**: aquí ponemos la región en la cúal estará nuestra instancia, en mi caso **us-west-2**.

 - **text_format**: aquí le di a **enter**, no es relevante de momento.

-----
### Uso de COMMANDO LINE INTERFACE
----


 Una vez especificado **Command Line Interface**, configuramos la conexión ssh con nuestra instacia, la cual crearemos en el Vagrantfile, para ello deberemos crear un archivo **.pem**. La documentación oficial de Amazon nos explica como realizarlo, concretamente [aquí](http://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-using-param.html). En mi caso me ha valido con seguir la siguiente sintaxis en la terminal:

```
aws ec2 create-key-pair --key-name my-key-pair --query 'KeyMaterial' --output text > my-key-pair.pem

```

**Nota**: el anterior comando guardará la clave de acceso por ssh en un archivo, en concreto en mi caso es **my-key-pair.pem**. Tenemos que tener apuntado la ruta en la cual tendremos este archivo porque se lo especificaremos cuando creemos la instancia de nuestra aplicación en el archivo **VagrantFile**. Hay que tener cuidado y no subirlo a nuestro repositorio ya que forma parte de los credenciales de nuestro perfil, al igual que los directivas rellenadas en **aws configure**. Para ello en **Vagrantfile** hago uso de **ENV['VARIABLE']**, más adelante lo veremos también.

Creamos un **Security Groups**, el cual usuará para atender peticiones. El apartado de la documentación oficial de Amazon de como crearlo se puede ver [aquí](http://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-ec2-sg.html). También hay que añadirle una serie de reglas para indicarle los puertos por los cuales va a atender(esta en el mismo apartado de la documentación oficial), en concreto yo he realizado los siguiente:

```
///Creación de Security Groups
 aws ec2 create-security-group --group-name my-sg --description "My security group"

 ///Configuración de la conexión por ssh
 aws ec2 authorize-security-group-ingress --group-name my-sg --protocol tcp --port 22 --cidr 0.0.0.0/0

 ///Configuracin de la conexión por http
aws ec2 authorize-security-group-ingress --group-name my-sg --protocol tcp --port 80 --cidr 0.0.0.0/0

```

![img8](https://www.dropbox.com/s/1haw0v9opo6wfmx/img8.png?dl=1)

Por lo que el apartado **inbound** de mi **Security Gropus** quedará de la siguiente forma:

![img6](https://www.dropbox.com/s/lyu7nn1cg1326cr/img6.png?dl=1)

El apartado **outbound** lo he dejado como estaba:

![img7](https://www.dropbox.com/s/5df40rptlt296ic/img7.png?dl=1)


---
### Creación de los archivos Vagrantfile y Ansible
---


Una vez realizado esto, modificamos nuestro **Vangranfile**, tiendo en cuenta:

 - Los datos del archivo **.csv** anterior.:

```
aws.access_key_id

aws.secret_access_key

```

 - Localización de nuestro sistema operativo:

```
aws.ami

```

 - Regíon de nuestra instancia:

```
aws.region



```

 - El nombre de nuestro archivo **.pem**:

```

keypair_name

```

- La ruta a nuestro archivo **.pem**:

```

private_key_path

```

 - El **security_groups** que se encargará de atender nuestras peticiones:

```
security_groups

```

 - El tipo de nuestra instancia, ** importante mirar las que son gratis o no**.

```
instance_type

```
 - El nombre del usuario de nuestra máquina:

```
override.ssh.username

```

**Nota**: Usuario por el cual se conectará por ssh, por defecto es **ubuntu** en EC2.


 - Por lo que podemos ver nuestro VangrantFile tendrá la siguiente estructura:


```
#-*- mode: ruby -*-
#vi: set ft=ruby :

Vagrant.require_plugin 'vagrant-aws'
Vagrant.require_plugin 'vagrant-omnibus'


Vagrant.configure('2') do |config|
    config.vm.box = "dummy"
    config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    config.vm.hostname = "Tiendas"

    config.vm.provider :aws do |aws, override|
        aws.access_key_id = ENV['ACCESS_KEY_ID']
        aws.secret_access_key = ENV['SECRET_ACCESS_KEY']
        override.ssh.private_key_path = ENV['PRIVATE_KEY_PATH']
        aws.keypair_name = "credenciales"
        aws.region = "us-west-2"
        aws.tags = {
          'Name' => 'Tiendas',
          'Team' => 'Tiendas',
          'Status' => 'active'
        }
        override.ssh.username = "ubuntu"

        aws.region_config "us-west-2" do |region|
          region.ami = 'ami-35143705'
          region.instance_type = 't2.micro'
          region.keypair_name = "credenciales"
          region.security_groups = "launch-wizard-3"
        end

        config.vm.provision "ansible" do |ansible|
          ansible.sudo = true
          ansible.playbook = "iv.yml"
          ansible.verbose = "v"
          ansible.host_key_checking = false
        end
    end
end


```

En el se diferencian tres partes:

- Primera: indica características del box de Vagrant y de la máquina virtual( especificaciones de la red, asignación del nombre de la máquina(en mi caso localhost)...).

- Segunda: la hemos explicado antes, son las características del provider de **EC2**.

- Tercera: es la parte de provisión, es decir, se indica que se quiere usar **ansible** y el archivo donde se quiere usar( en mi caso **iv.yml**).

Si se tiene alguna duda, se puede consultar el siguiente [enlacen](https://github.com/mitchellh/vagrant-aws).


 - Como podemos ver, para desplegar la aplicación estamos usando **ansible**, este se encarga de instalar todos los paquetes necesarios, descargar nuestra aplicación de nuestro repositorio y ejecutarla, concretamente mi archivo **.yml** es el siguiente:

```
- hosts: localhost
  remote_user: ubuntu
  sudo: true
  tasks:
  - name: Actualizar sistema
    apt: update_cache=yes upgrade=dist
  - name: Instalar python-setuptools
    apt: name=python-setuptools state=present
  - name: Instalar build-essential
    apt: name=build-essential state=present
  - name: Instalar pip
    apt: name=python-pip state=present
  - name: Instalar git
    apt: name=git state=present
  - name: Ins Pyp
    apt: pkg=python-pip state=present
  - name: Instalar python-dev
    apt: pkg=python-dev state=present
  - name: Instalar libpq-dev
    apt: pkg=libpq-dev state=present
  - name: Instalar python-psycopg2
    apt: pkg=python-psycopg2 state=present
  - name: Obtener aplicacion de git
    git: repo=https://github.com/lorenmanu/Tiendas.git  dest=/home/ubuntu/Tiendas clone=yes force=yes
  - name: Permisos de ejecucion
    command: chmod -R +x Tiendas
  - name: Instalar libreria para pillow
    command: sudo apt-get -y build-dep python-imaging --fix-missing
  - name: Instalar pillow
    command: sudo easy_install Pillow
  - name: Instalar requisitos
    command: sudo pip install -r Tiendas/requirements.txt
  - name: ejecutar
    command: nohup sudo python Tiendas/manage.py runserver 0.0.0.0:80

```

---
### Despliegue de la aplicación
---

Como se puede ver en el archivo **Vagrantfile** hago uso de **ENV['NOMBRE-PRIMITIVA']**, esto se debe a que aprovecho la posibilidad que me da **Vagrant** de pasar parámetros al archivo para introducir los credenciales de **Amazon**. Las variables se introducen cuando creemos o destruyamos la instancia siguiendo la siguiente sintaxis:

```
var=valor vagrant up/destroy --provider=aws
----------------------------------------------------
//Referencia en Vagrantfile

ENV['var']

```

En el caso de mi proyecto se debería poner:

```
// Para crear la instancia
 sudo ACCESS_KEY_ID="valor" SECRET_ACCESS_KEY="valor" PRIVATE_KEY_PATH="valor" PRIVATE_KEY_NAME="valor" SECURITY-GROUPS="valor" vagrant up --provider=aws

// Para destruir la instancia

sudo ACCESS_KEY_ID="valor" SECRET_ACCESS_KEY="valor" PRIVATE_KEY_PATH="valor" PRIVATE_KEY_NAME="valor" SECURITY-GROUPS="valor" vagrant destroy

```

He proporcionado un archivo que nos permite descargarnos la aplicación y desplegarla en la carpeta **scritps**, en concreto se puede ver [aquí](https://github.com/lorenmanu/Tiendas/blob/master/scripts/deploy_EC2.sh). Para ejecutarlo se debería poner en la terminal lo siguiente(dentro del directorio donde este el archivo):

```

 sudo ACCESS_KEY_ID="valor" SECRET_ACCESS_KEY="valor" PRIVATE_KEY_PATH="valor" PRIVATE_KEY_NAME="valor" SECURITY-GROUPS="valor" ./desploy_EC2.sh

```

**Nota**: en **--provider** estamos indicando el proveedor, en mi caso Amazon, si fuera Azure deberíamos poner **azure**.


- Finalmente nuestra aplicación estará desplegada:

![img21](https://www.dropbox.com/s/w6s217d4pld9o0j/img24.png?dl=1)

**Nota**: el archivo **Vagranfile** y **.yml(ANSIBLE)** se encuentran en la carpeta VagrantIV del repositorio de la aplicación. Si queremos desplegarla deberemos realizar los pasos anteriormente descritos en este directorio de la aplicación(anteriormente descargada **git clone htttp...**). He proporcionado un **archivo** también por si se quiere desplegar sin hacer uso de **vagrant up --provider=aws**, en conreto usuando este archivo la sintaxis sería:

```

var=valor ./create_and_run.sh
----------------------------------------------------
//Referencia en Vagrantfile

ENV['var']



```


----------


### Referencias


----------


- Documentación oficial **AWS**: [ENLACE](https://aws.amazon.com/es/documentation/ec2/).

- Uso de vagrant y ansible: ayudado por el enlace del profesor, y de un github en inglés:

    - [Enlace profesor](https://twitter.com/jjmerelo/status/688335964947779584).
    - [Github en inglés](https://github.com/mitchellh/vagrant-aws).

- Uso de **CLI**: documentación oficial de Amazon.
    - [ENLACE](http://docs.aws.amazon.com/cli/latest/reference/ec2/).

- Conocimientos básicos de Vagrant, sobre todo **la primera parte anteriormente mencionada**.
    - [ENLACE](https://geekytheory.com/tutorial-vagrant-1-que-es-y-como-usarlo/).
