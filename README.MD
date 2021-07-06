# FCRY.PY
<p align="center">
 <br></br>
 <img src="https://www.python.org/static/img/python-logo.png">
</p>

## REQUISITOS
Para poder ejecutar y probar este script es necesario contar con una instalación de Python mayor a 3.X, es recomendable que se realice en un entorno seguro y controlado para este tipo de pruebas donde no se ponga en riesgo ningún archivo o documento de suma importancia.

Lo que necesitas instalar:
- [Python 3.X](https://www.python.org/) :snake:
- Opcional [VirtualBox](https://www.virtualbox.org/) :package:
- Recomendado [VSCode](https://code.visualstudio.com/) :computer:
- Cualquier sistema operativo Windows :computer: o basado en Linux :penguin:

También necesitarás tener archivos de prueba dentro de tu sistema para que puedas comprobar la eficacia del script.

## PASOS A SEGUIR PARA SU CORRECTO FUNCIONAMIENTO
Una vez tengas instalada tu versión de python 3.X puedes utilizar la CL de [GIT](https://git-scm.com/) para clonar este repositorio o bien descargar directamente una copia desde el botón verde que dice "Code" en la opción "Download ZIP"

###### UTILIZANDO LA CLI DE GIT
Deberás pocicionarte en la carpeta donde desas clonar el repositorio y estando allí ejecutar el comando:
```
git clone https://github.com/Fernand117/fcry.git
```

###### INSTALANDO LIBRERÍAS ADICIONALES
Para correr este script es necesaria la instalación de las siguientes librerías

Cryptography
```
python3 -m pip install cryptography
```

Colorama
```
python3 -m pip install colorama
```

###### EJECUCIÓN
Una vez clonado el repositorio entrar desde tu terminal (Windows/Linux) y ejecutar:
```
python3 fcry.py
```
Cuando se empiece a ejecutar el script te mostrará en pantalla la lista de directorios y archivos a modificar que se le han dado por defecto.

## ¿CÓMO FUNCIONA?
Este "ransomware" ataca directamente a la carpeta raíz del usuario ya sea que se encuentre en Windows o Linux, en su primera versión no hace uso de alguna vulnerabilidad existente en ambos sistemas, por lo que las funciones principales del SO están intactas, siendo los archivos personales del usuario los afectados tras el ataque. Cuando el script termina de escanear todos los directorios este los encrypta cada uno de los archivos existentes generando una key que se almacena en algún lugar del sistema dejando inutilizables los archivos a no ser que se realice la accción contrario al proceso principal.

###### PROCESO DE EJECUCIÓN

1. Obtiene información del sistema como lo es el Usuario y el tipo de S.O.
2. Válida el tipo de S.O en el que se está ejecutando el script para poder llamar a la función acorde al tipo de S.O.
3. Una vez detectado el tipo de S.O, lista todos los directorios del usuario añadiendo sus archivos y carpetas a un arreglo.
4. En el caso de Windows realiza un par de validaciones puesto que hay carpetas y archivos protegidos por el sistema.
5. El script comenzará a encryptar y moficiar los archivos escaneados y al finalizar mostrará un mensaje similar a Completado!!
6. Una vez se termine de ejecutar todo, en el escritorio dejará un archivo .txt con nombre README.txt

## NOTA IMPORTANTE
Este script es creado con fines educativos, el uso mal intencionado que se le pueda dar a este script no es mi responsabilidad, por tanto, la persona que haga mal uso de este, será el responsable directo por su ejecución.

<p>Es importante recalcar que no se debe ejecutar en un sistema operativo funcional ya que podría dañar sus archivos y a pesar de que se pueden desencryptar los archivos con la KEY que se genera, este script no incluye la función que permite realizar dicha acción ;).</p>
<p>Puedes modificar la función que crea el archivo READMEH.txt para ponerle lo que quieras</p>
<p>Puedes realizar modificaciones al código, sobre todo en la parte de los directorios.</p>

## GRACIAS
<p>Creado por Luis Fernando Leyva Luna</p>
<p>Sígueme en Instagram: [@fernand_117](https://www.instagram.com/fernand_117/?hl=es-la)</p>
