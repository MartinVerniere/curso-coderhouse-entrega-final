# Proyecto Final
Este es el proyecto final realizado para el curso de Python en Coderhouse.

## Pasos para ejecutar el proyecto
- Obtener el archivo desde el repositorio en Github()

- Estando parados en la carpeta principal del proyecto (donde se encuentran "myapp" y "Entrega Final"), ejecutar el comando "./myenv/scripts/Activate"

- Estando en el ambiente virtual, proceder a ejecutar el comando "pip install -m requirements.txt", para instalar los paquetes necesarios

- Luego de instalar los paquetes, para ejecutar la aplicacion en un servidor local debe ejecutar en la consola el comando "python manage.py runserver", y se podra ingresar al programa utilizando localhost en el navegador

## Probar la app de Django
- Para probar la app, puede hacer click en uno de los botones de la pagina de inicio, o de los botones del navegador, que lo redireccionaran a las URLs que muestran un listado para cada elemento.

- Haciendo click en "Crear vehiculo" en el navbar (o llendo a la pagina de vehiculos y hacer click en "Añadir Vehiculo") puede añadir un nuevo vehiculo llenando un formulario.

- Estando en la pagina de listado de vehiculos, utilizando el campo de busqueda puede filtrar los resultados que se mostraran (se filtran por marca y modelo, todos los vehiculos cuya marca o modelo contengan la palabra buscada se mostraran).

- Si quiere que se muestren todos los resultados deje el campo de busqueda vacio y haga click en "Buscar".

## Estructura del codigo
- Dentro de /EntregaFinal se encuentra la configuracion relacionada al proyecto.

- Dentro de /templates hay un archivo base.html con la estructura general de la aplicacion, con un navbar superior para navegacion.

- En /myapp se encuentra la configuracion relacionada a la app.
    - En el archivo models.py se detallan los modelos utilizados.
    - En el archivo views.py se detallan las vistas utilizadas.
    - En el archivo forms.py se detallan los formularios utilizados.
    - En el archivo urls.py se detallan las url utilizadas para acceder a las vistas.
    - Dentro de templates/myapp se encuentran los archivos html, que extienden al archivo base.html, relacionados a la pagina de home y a la pagina de "about me" y tambien los de las paginas relacionadas a la creacion/eliminacion/detalle/actualizacion de los vehiculos.

- Dentro de /profiles se encuentra la configuracion relacionada a las paginas de autenticacion de usuarios, con estructura similar a los archivos en /myapp.

- Dentro de /static se encuentran paquetes de ckeditor necesarios para mostrar algunas utilidades de la pagina (por ejemplo RichTextField).

- Dentro de /media se guardan las imagenes de los avatares de los usuarios o de los vehiculos guardados

## Adicionales
- Por como esta realizado el formulario de creacion/actualizacion, la imagen cargada no se podra ver en ese momento, sino que se actualizara cuando se guarden los cambios y se quiera ver la imagen en detalles o actualizar.