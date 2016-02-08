### Acceso Remoto y Automatización con Fabric

Para realizarlo tendremos que tener creada una instancia en ec2, la explicación de su creación se detalla en **ec2.md** en la carpeta documentación del proyecto. Los pasos realizados para el despliegue son:

- **Primero**: instalar **Fabric**. Bastará con poner en la terminal:

```
sudo pip install fabric

```

- **Segundo**: Localizar nuestro archivo con la clave privada proporcionada por Amazon. Este archivo tendrá extensión **.pem** y Amazon nos permitirá su descarga cuando [creemos la instancia](https://github.com/lorenmanu/Tiendas/blob/master/documentacion/ec2.md). Copiaremos la ruta a dicho archivo y lo añadiremos a la conexíon **ssh** con el siguiente comando:

```
ssh-add "ruta archivo"

```
En el siguiente pantallazo muestro como Amazon me indica realizar la conexión ssh, con el correspondiente archivo(**extensión .pem**), como lo busco y lo añado a ssh.

![img1](https://www.dropbox.com/s/exnxucut9noig86/img1_iv.png?dl=1)

**Nota**: antes de añadir el archivo a ssh debemos ponerle los permisos adecuados, por lo que en la terminal indicaremos:

```
chmod 400 "nombre_archivo".pem

```

- **Tercero**: Una vez realizado el paso anterior, me dispongo a usar mi archivo **fabfile.py**. En este archivo tengo diferentes tareas automatizadas para realizarlas por ssh. Para ello, tendremos que dirigirnos al directorio donde se encuentra el archivo **fabfile.py** y seguir la siguiente sintaxis en la terminal:

```
fab -H NombreUsuario@Nombredelhost/o/IPelhost operación

```

Las operaciones que permite realizar mi **fabfile.py** son:

- Obtener información del host:
![img2](https://www.dropbox.com/s/lvkbxodkdqcmj3k/img2_iv.png?dl=1)

- Descargar la aplicación:
![img3](https://www.dropbox.com/s/67dmce3q2tah8hc/img3_iv.png?dl=1)

- Instalar las dependencias:
![img4](https://www.dropbox.com/s/glgtkxdd20tomyh/img4_iv.png?dl=1)

- Sincronizar la base de datos:
![img5](https://www.dropbox.com/s/atad1g9cs1taf5p/img5_iv.png?dl=1)

- Realizar los tests en local:
![img6](https://www.dropbox.com/s/loi6aznjpgmdlrl/img6_iv.png?dl=1)

- Ejecución de la aplicación:
![img7](https://www.dropbox.com/s/insyi6vmy5vsuzj/img7_iv.png?dl=1)

**Nota**: como se puede ver en la anterior imagen se ha ejecutado la aplicación y accedido a ella por el navegador desde el DNS que nos da Amazon. Esto es posible si configuramos las reglas correctamente, se detalla en [**documentacion/ec2.md**](https://github.com/lorenmanu/Tiendas/blob/master/documentacion/ec2.md).


### Despliegue con docker.

Si queremos realizar el despliegue usando el docker, bastará con usar las operaciones del archivo **fabfile.py** para ese propósito:

- Descarga del docker:
![img8](https://www.dropbox.com/s/0mqlavcpcgi3ux6/img8_iv.png?dl=1)
- Ejecutar docker:
![img9](https://www.dropbox.com/s/wab4995g1vzk5k5/img9_iv.png?dl=1)

Con la opción **-p 80:80** estamos indicando que las peticiones que lleguen por el puerto **80** a la instancia se dirigan al puerto **80** del docker. Se puede ver más detallado en la documentación oficial de Amazon en el siguiente [apartado](http://docs.aws.amazon.com/es_es/AmazonECS/latest/developerguide/docker-basics.html).



### Comprobación
El enlace de mi app en ec2 de Amazon mediante automatización se puede ver [aquí](http://ec2-52-11-219-71.us-west-2.compute.amazonaws.com).

### Aclaración

Las imágenes mostradas en este apartado son antiguas, es decir, que se ha migrado la aplicación ha otra instancia **ec2** usando como herramienta de despliegue **vagrant** y **ansible**. Para más información se puede consultar el **README** de la aplicación. El motivo fundamental por el cual lo he hecho es porque **Amazon** solo permite tener como versión gratuita 750 horas al mes una solo instancia.
