## Creación de Docker ##

Lo primero es tener un archivo **DockerFile** para la creación de la imagen, el mio se puede ver [aquí](https://github.com/lorenmanu/Tiendas/blob/master/Dockerfile).


Después se despliega nuestra aplicación en docker-hub, para ello se sigue los siguientes pasos:
- Registro en [hub.docker.com](https://hub.docker.com/add/automated-build/github/orgs/?namespace=lorenmanu).

- Una vez registrados le daremos a **Create/Create Automated Build** en el repositorio del proyecto. Aquí tardará un poco ya que se estará construyendo la imagen.

- Una vez creada la imagen, podremos ver:

- El repositorio enlazado:

![img2](https://www.dropbox.com/s/f1wgql8u3yeopga/img2.png?dl=1)

- Construcción de la imagen:

![img3](https://www.dropbox.com/s/no7qfjlxqhy43ot/img3.png?dl=1)

**Nota**: cada vez que realicemos un **git push** en el repositorio se integrará de manera automática en **dockerhub**.

Para obtener el **docker** en nuestro ordenador he proporcionado un archivo en la carpeta **scripts**, puede verse [aquí](https://github.com/lorenmanu/Tiendas/blob/master/scripts/docker_install_and_run.sh). Lo que hace este archivo es lo siguiente:

- Instalar docker:

```

sudo apt-get update
sudo apt-get install -y docker.io

```

- Crear el contenedor con la aplición instalada:

```
sudo docker pull lorenmanu/tiendas

```

- Ejecutarlo:

```

sudo docker run -t -i lorenmanu/Tiendas /bin/bash

```

Una vez dentro cuando lo ejecutamos, solo quedaría ejecutar la aplicación, para ello nos dirigiremos al directorio donde se localice **manage.py** y pondremos en la terminal:

```

python manage.py runserver 0.0.0.0:1111

```

Cuando hagamos esto, para ver la aplicación ejecutada desde el navegador anfitrión deberemos poner la **IP** del docker:

![img4](https://www.dropbox.com/s/3ff17lnfuf1977e/img4.png?dl=1)
