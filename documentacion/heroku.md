


## **Como subir nuestra aplicación a heroku** ##



- Descargar del toolbelt de heroku:

```

wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   

```

- Crear un archivo Procfile, en el cual se indica a heroku que se quiere iniciar una instancia web, y dejar que gunicorn ejecute nuestra aplicación dentro de ella:

```
web: gunicorn MiTienda.wsgi --log-file -

```

- Realizar login(se pedirá credenciales):

```

heroku login

```


- Crear la aplicación:

```

heroku create

```

- Subir los cambios que se realicen a heroku:

```

git add .
git commit -m "subir aplicación"
git push heroku master

```
- Indicar que se quiere usar la base de datos que creemos en heroku( en mi caso **PostgreSQL**). Se tiene que añadir al archivo settings.py lo siguiente:

```

import dj_database_url

...

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
ON_HEROKU = os.environ.get('PORT')
if ON_HEROKU:
    DATABASE_URL=' postgres://qcgsjyjlrxrbut:AB6HfA2cXIV74B8z_xKl-V88vI@ec2-107-21-219-109.compute-1.amazonaws.com:5432/df1bb3foip112r'
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

...

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


```

- En **wsgi.py** poner lo siguiente:

```

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MiTienda.settings")

#from whitenoise.django import DjangoWhiteNoise
application = get_wsgi_application()


application = Cling(get_wsgi_application())
#application = DjangoWhiteNoise(application)

```

Aclaraciones sobre la modificación del archivo **settings.py**:

- En DATABASE_URL se indica la url de la base de datos postgreSQL de Heroku( que deberemos haber creado antes), hay que darle a show para verlo.

- Para actualizar y/o sincronizar la base de datos se debe poner en la terminal lo siguiente:
 - **heroku run python manage.py makemigrations**
 - **heroku run python manage.py migrate**
 - **heroku run python manage.py createsuperuser**.

También cabe destacar que hemos usado **snap-ci**. Snap-ci me permitirá sincronizar a nuestro repositorio, y de esta forma se desglosará un pipeline con los distintos estados por los que se pasa hasta el despliegue:

- Instalación de las dependencias.
- Ejecución de los tests.
- Despliegue.

![img5](https://www.dropbox.com/s/btqs6ub1j3uacqd/img5.png?dl=1)





**Nota**: para abrir la aplicación en el navegador, tendremos que es escalar el **dynos** de heroku, para ello ponemos en la terminal:


```
heroku ps:scale web=1 \\escalamos dynos

heroku open \\ abrimos aplicación

```
