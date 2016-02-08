### Creación de la instancia ec2 con su aplicación web dando servicio

Una vez registrados en Amazon, donde tendremos que dar una tarjeta de crédito y seguir una serie de trámites(son muy estrictos para mi gusto), se procede a crear una instancia, para ello se siguen los siguientes pasos:

- Nos dirigimos al apartado **EC2 VIRTUAL SERVERS IN THE CLOUD**.

![img10](https://www.dropbox.com/s/2bfpzbkdlo2ygyx/img10_iv.png?dl=1)

- Pinchamos en **Instances**.

![img11](https://www.dropbox.com/s/fhmkr9dfmot239l/img11_iv.png?dl=1)

- Le damos a la pestaña **Launch Instance**.

![img12](https://www.dropbox.com/s/luntkxme7qtzxgi/img12_iv.png?dl=1)

**Nota**: despúes del proceso de seleccionar las carácterísticas de nuestra máquina  nos descargaremos un archivo en extensión **.pem**, que contendrá la clave secreta y nos permitirá realizar la conexión a nuestra instancia por ssh. Amazon ya nos da instruciones sobre su uso si pinchamos en la pestaña **Connect**, pero podemos añadir la clave a nuestra configuración ssh de tal manera que solo tengamos que introducir en la terminal ** ssh usuario@nombre_dns_instancia_amazon.com ** para poder conectarnos a nuestra instancia remotamente, será necesario introducir en la terminal:

```
ssh-add ruta_archivo.pem

```

- Cuando tengamos la máquina, tendremos que indicar las peticiones que queremos atender, por lo que nos vamos a la pestaña **description** en el apartado **Security groups** y copiamos el nombre que tiene(en mi caso es **launch-wizard-3**). En esta pestaña también podemos encontrar otra información relevante, como puede ser la ip pública, el dns que nos da Amazon...

![img14](https://www.dropbox.com/s/d5jgusar1pe9mw2/img14_iv.png?dl=1)

- En **Security groups**, seleccionamos el nombre que está sombreado en azul de la anterior imagen y hacemos click a la pestaña **Inbound**, como se pude observar hay una serie de reglas que podemos editar para eliminarlas o añadir más.

![img15](https://www.dropbox.com/s/d95pnycmw0fuqky/img15_iv.png?dl=1)

![img16](https://www.dropbox.com/s/2190m8k8ks0ao8w/img16_iv.png?dl=1)
**Nota**: Yo he configurado mi máquina para que pueda atender peticiones realizadas por shh y http.

- Ya tan solo nos quedaría arrancar nuestro servidor. En mi caso me tendría que dirigir al directorio donde está el archivo **manage.py** y poner en el la terminal:


```

sudo python manage.py runserver 0.0.0.0:80

```

Esto último lo tenemos automatizado...

### ¿Cómo se hace lo anterior automatizado ?

En la anterior explicación hemos visto como hacer que nuestra aplicación de servicio de manera manual. Este proceso se puede automatizar usando la biblioteca de python fabric. Esta automatización puede hacer que nuestra instancia en Amazon de servicio desde la misma máquina( similar al servicio anterior) o desde un docker. Se puede ver como hacerlo en el siguiente [archivo](https://github.com/lorenmanu/Tiendas/blob/master/documentacion/fabfile.md).
