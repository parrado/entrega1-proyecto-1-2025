<h1 align="center">
Lab 2: Servidor de Jugadores y Preguntas (RA 1, RA 3) <br />
 </h1>
 <p align="center">
Alexander López-Parrado, PhD. <br />
Programación, II-2024 <br />
GDSPROC <br />
Uniquindío <br />
</p>

Con esta práctica se iniciará el desarrollo del código fuente en Python del proyecto del espacio académico. En este caso, y de acuerdo a la arquitectura mostrada en la siguiente figura, se construirá el código del lado del servidor para la gestión de jugadores y preguntas.

<p align="center">
<img  src="Programación-II-2024.png" width="800" >
</p>
En ese sentido, la práctica de laboratorio contempla la creación y prueba de funciones que hacen uso de archivos para la gestión de los jugadores y las preguntas, así como las demás estructuras de programación y tipos de datos estudiados hasta el momento. 

## Código base suministrado

Se suministra el código base del servidor en el archivo [trivia_server.py](trivia_server.py) el cual contiene toda la funcionalidad para que éste opere dentro de una red de área local o en el mismo equipo de prueba. **Este archivo no debe ser modificado bajo ninguna circunstancia**.

En ese sentido, el archivo [trivia_server.py](trivia_server.py) usa el archivo [users.py](users.py) que incluye definiciones de funciones las cuales deben ser implementadas en el laboratorio de acuerdo a los descrito en los comentarios del archivo. **La implementación de estas funciones y su correcto funcionamiento determina la evaluación de esta práctica de laboratorio y el lado del servidor del proyecto**.

El servidor permite registrar usuarios con un nombre y contraseña, y una vez un usuario registrado inicie sesión podrá:

* Actualizar su puntaje y obtener su puntaje actual.
* Obtener la lista de usuarios conectados con sesión iniciada.
* Solicitar una pregunta aleatoria desde una categoría.
* Cerrar sesión.

También, se suministran los archivos [trivia_client.py](trivia_client.py) y [test_trivia_client.py](test_trivia_client.py). En este caso, [trivia_client.py](trivia_client.py) implementa la funcionalidad básica de los clientes (jugadores) para la conexión con el servidor por lo que **no debe ser modificado bajo ninguna circunstancia**. De otro lado, [test_trivia_client.py](test_trivia_client.py) es un archivo de prueba que se suministra para verificar el correcto funcionamiento del servidor y que puede ser modificado a gusto de los miembros del equipo. Para que [trivia_client.py](trivia_client.py) pueda funcionar correctamente se debe instalar el módulo de Python requests ejecutando el siguiente comando en una terminal:

``` pip install requests```

## ¿Cómo realizar las pruebas?

Para la realización de las pruebas debe ejecutar primero el programa [trivia_server.py](trivia_server.py), la recomendación es verificar el correcto funcionamiento de las funciones, una a la vez. Posteriormente se puede ejecutar el programa [test_trivia_client.py](test_trivia_client.py), en caso de que se creen ventanas emergentes de Windows solicitando permisos, por favor otorgarlos ya que los programas hacen uso de los servicios de red. 

Tenga en cuenta que es posible que [trivia_server.py](trivia_server.py) y [test_trivia_client.py](test_trivia_client.py) se ejecuten en computadores diferentes siempre y cuando los equipos se encuentren conectados a la misma red LAN cableada o inalámbrica. En ese caso basta con consultar la dirección IP del computador que está ejecutando [trivia_server.py](trivia_server.py) mediante el comando ipconfig como se muestra en la siguiente figura.


<p align="center">
<img  src="Captura de pantalla (2).png" width="800" >
</p>

La IP encontrada debe sustituir "localhost" en la línea 6 de [test_trivia_client.py](https://github.com/parrado/lab2/blob/c80a0f73b9324b082ebea63a3377358d36a4c8d8/test_trivia_client.py#L6)

# Entrega del laboratorio

El laboratorio debe ser presentado mediante:

1. Repositorio en GitHub.
2. Informe de laboratorio.

El informe de laboratorio y el enlace al repositorio de GitHub deben ser compartidos en el enlace dispuesto para tal fin en la plataforma Google Classroom.
