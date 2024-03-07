# Manual del usuario

Esta es la documentación oficial para el uso del supercomputador Picasso. Si tienes algún problema que no esté especificado en esta documentación o en la sección de [preguntas frecuentes](#sec_7), por favor, ponte en contacto a través de

```
soporte@scbi.uma.es.
```

# Índice

- [1 - Cita y agradecimientos](#sec_1)
- [2 - Acerca de Picasso: Hardware y Sistemas de Ficheros](#sec_2)
    - [2.1 - Vista general del sistema](#sec_2.1)
    - [2.2 - Recursos de hardware](#sec_2.2)
        - [2.2.1 - Recursos totales de cómputo](#sec_2.2.1)
        - [2.2.2 - Recursos disponibles](#sec_2.2.2)
    - [2.3 - Sistema de ficheros](#sec_2.3)
        - [2.3.1 - Sistemas de ficheros de Picasso](#sec_2.3.1)
        - [2.3.2 - Cuotas de ficheros y espacio](#sec_2.3.2)
        - [2.3.3 - Sistema de ficheros de scratch rápido (FSCRATCH)](#sec_2.3.3)
        - [2.3.4 - Sistema de ficheros de scratch local](#sec_2.3.4)
        - [2.3.5 - Política de respaldo](#sec_2.3.5)
- [3 - Inicio de sesión en Picasso](#sec_3)
    - [3.1 - Conexión SSH](#sec_3.1)
    - [3.2 - Terminal](#sec_3.2)
    - [3.3 - Aviso importante](#sec_3.3)
- [4 - Cómo enviar trabajos](#sec_4)
    - [4.1 - Preparación para enviar un trabajo](#sec_4.1)
    - [4.2 - Modificación de recursos y límites](#sec_4.2)
    - [4.3 - Solicitud de GPUs](#sec_4.3)
    - [4.4 - Generador de trabajos de ejemplo](#sec_4.4)
    - [4.5 - Envío de un trabajo](#sec_4.5)
    - [4.6 - Trabajos en serie: cómo enviar muchos trabajos](#sec_4.6)
    - [4.7 - Monitoreo de trabajos en cola](#sec_4.7)
        - [4.7.1 - Comando Squeue](#sec_4.7.1)
        - [4.7.2 - Nuevo monitoreo de trabajos en línea](#sec_4.7.2)
    - [4.8 - Cancelación de trabajos](#sec_4.8)
    - [4.9 - Uso del sistema de ficheros LOCALSCRATCH](#sec_4.9)
- [5 - Copiar ficheros desde/hacia Picasso](#sec_5)
    - [5.1 - Descarga de ficheros desde internet](#sec_5.1)
        - [5.2.1 - Comando Scp](#sec_5.2.1)
        - [5.2.2 - Comando Rsync](#sec_5.2.2)
    - [5.2 - Copia de ficheros desde tu computadora a Picasso y viceversa](#sec_5.2)
- [6 - Software](#sec_6)
    - [6.1 - Software instalado](#sec_6.1)
    - [6.2 - Cómo cargar/descargar software](#sec_6.2)
        - [6.2.1 - Cargar software](#sec_6.2.1)
        - [6.2.2 - Listar el software cargado](#sec_6.2.2)
        - [6.2.3 - Descargar software](#sec_6.2.3)
    - [6.3 - Compilación de software](#sec_6.3)
- [7 - Comandos propios de Picasso](#sec_7)
- [8 - Preguntas frecuentes](#sec_8)
    - [8.1 - ¿Cuántos recursos debería solicitar para mis trabajos?](#sec_8.1)
    - [8.2 - Mensaje de error: Conection refused/The network is not available](#sec_8.2)
    - [8.3 - Mensaje de error: Remote host identification has changed](#sec_8.3)
    - [8.4 - ¿Cómo cambio mi contraseña?](#sec_8.4)
    - [8.5 - ¿Por qué mi proceso en el nodo de inicio de sesión está siendo detenido?](#sec_8.5)
    - [8.6 - ¿Por qué mi trabajo está en cola durante tanto tiempo?](#sec_8.6)
    - [8.7 - ¿Por qué mi trabajo no obtiene los recursos que solicité?](#sec_8.7)
    - [8.8 - Necesito más tiempo para mi trabajo](#sec_8.8)
    - [8.9 - ¿Por qué ha fallado mi trabajo?](#sec_8.9)
    - [8.10 - Mensaje de error: cnf <comando>](#sec_8.10)
    - [8.11 - ¿Por qué se ha cancelado mi trabajo?](#sec_8.11)
    - [8.12 - Mensaje de error: Out of memory handler](#sec_8.12)
    - [8.13 - ¿Por qué no puedo editar ni crear nuevos ficheros?](#sec_8.13)
    - [8.14 - Necesito más espacio o cuota de ficheros](#sec_8.14)


[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)



# 1 - Cita y agradecimientos <a id="sec_1"></a>

Si utilizas nuestros recursos, debes dar reconocimiento a este servicio en tus publicaciones. Por favor, agrega un texto como este:

    El autor reconoce y agradece los recursos informáticos, la experiencia técnica y la asistencia 
    proporcionada por el centro de Supercomputación y Bioinformática (SCBI) de la Universidad de Málaga.

Por favor, infórmanos sobre aquellas publicaciones que utilizaron nuestros recursos, ya que esto nos permite solicitar ampliaciones para Picasso, de las que también te podrás beneficiar. Aprovecharemos la oportunidad para felicitarte.

[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)



# 2 - Acerca de Picasso: Hardware y Sistemas de Archivos <a id="sec_2"></a>

## 2.1 - Visión general del sistema <a id="sec_2.1"></a>

Los recursos de supercomputación del SCBI comprenden un conjunto de nodos de computación con diferentes características. Sin embargo, todas esas máquinas están unificadas detrás del sistema de colas **Slurm**, por lo que no tendrás que preocuparte por sus diferencias. Bastará con crear un script SBATCH (un archivo de texto con una sintaxis especial).

El script se utiliza para **solicitar los recursos** (tiempo, CPUs, memoria, GPUs, etc.) de los que tu trabajo hará uso. Es importante que los recursos solicitados puedan utilizarse de manera óptima, ya que esto facilitará que tu trabajo empiece a resolver lo antes posible. Las máquinas con características especiales como más memoria o GPUs son escasas, y debido a esto son más difíciles de reservar.

Una vez que tengas tu script escrito, debes enviarlo al **sistema de cola**. Luego, el sistema de cola analizará tu solicitud y enviará el trabajo a las computadoras apropiadas. Hay algunos ejemplos en el capítulo [Cómo enviar trabajos](#sec_4). Si tienes alguna pregunta, por favor, no dudes en contactarnos en soporte@scbi.uma.es y haremos todo lo posible para ayudarte.

## 2.2 - Recursos de hardware <a id="sec_2.2"></a>

### 2.2.1 - Recursos totales de cómputo <a id="sec_2.2.1"></a>

En Picasso tenemos los siguientes nodos:

- **Nodos sd**: 126 x nodos SD530: 52 núcleos (Intel Xeon Gold 6230R @ 2.10GHz), 192 GB de RAM. Red InfiniBand HDR100. 950 GB de discos localescratch.
- **Nodos bl**: 24 x nodos Bull R282-Z90: 128 núcleos (AMD EPYC 7H12 @ 2.6GHz), 2 TB de RAM. Red InfiniBand HDR200. 3.5 TB de discos localescratch.
- **Nodos sr**: 156 x nodos Lenovo SR645: 128 núcleos (AMD EPYC 7H12 @ 2.6GHz), 512 GB de RAM. Red InfiniBand HDR100. 900 GB de discos localescratch.
- **Nodos bc**: 34 x nodos Lenovo SR645 v3: 256 núcleos (AMD EPYC 9754 @ 2.25GHz), 768 GB de RAM. Red InfiniBand 2x HDR200. 4 TB de discos localescratch.
- **Nodos exa (GPU)**: 4 x nodos DGX-A100: 8 GPUs (Nvidia A100), 1 TB de RAM. Red InfiniBand HDR200. 14 TB de discos localscratch.

### 2.2.2 - Recursos disponibles <a id="sec_2.2.2"></a>

Tanto el sistema operativo como el sistema de ficheros requieren parte de los recursos (RAM) disponibles en los nodos. Por esta razón, los recursos (CPUs, RAM) que se pueden solicitar para cada nodo a través del sistema de cola son los siguientes:

- **Nodos sd**: CPUs: 52 núcleos. RAM: 182 GB.
- **Nodos bl**: CPUs: 128 núcleos. RAM: 1855 GB.
- **Nodos sr**: CPUs: 128 núcleos. RAM: 439 GB.
- **Nodos bc**: CPUs: 256 núcleos. RAM: 683 GB.
- **Nodos exa (GPU)**: CPUs: 128 núcleos. RAM: 878 GB.

<span style="color: red"> IMPORTANTE </span>: Los recursos de los nodos Exa se distribuyen entre las 8 GPUs de cada nodo, por lo que en el uso ideal no se deben solicitar más de 16 núcleos y 109 GB de RAM por GPU solicitada.

<span style="color: red"> IMPORTANTE </span>: Si tienes la intención de utilizar muchos ficheros (por ejemplo, más de 15000) para resolver un problema (por ejemplo, en entrenamiento de IA), debes contactar con nosotros primero, ya que puede provocar problemas graves en el rendimiento general de Picasso.

## 2.3 - Sistema de ficheros <a id="sec_2.3"></a>

### 2.3.1 - Sistemas de ficheros de Picasso <a id="sec_2.3.1"></a>

El sistema de ficheros de Picasso está dividido en dos espacios físicamente independientes. En ambos, como usuario de Picasso, obtendrás una cuota de disco

- **HOME** (*Sistema de almacenamiento permanente*): Aquí deberías almacenar datos de entrada, tus propios scripts desarrollados, resultados finales y otros datos importantes. Para volver a tu home, puedes ingresar alguno de los siguientes comandos:

```
    cd
```
```
    cd ~
```
```
    cd $HOME
```
- **FSCRATCH** (*Sistema de almacenamiento temporal*): FSCRATCH es un almacenamiento de alta velocidad en el que deberías lanzar tus trabajos. Puedes encontrar información relevante sobre el uso de FSCRATCH en la sección [Sistema de ficheros de scratch rápido (FSCRATCH)](#sec_2.3.3). Ten en cuenta que FSCRATCH es un almacenamiento temporal, y los ficheros antiguos se eliminarán periódicamente. <span style="color: red"> POR FAVOR, NO LO USES PARA ALMACENAR DATOS IMPORTANTES </span>. Para ir a tu espacio de fscratch puedes ingresar:

```console
    cd $FSCRATCH
```



### 2.3.2 - Cuota de ficheros y espacio <a id="sec_2.3.2"></a>

Además de la **limitación de espacio** en cada uno de los dos espacios (home y fscratch), también hay una **cuota de ficheros**. Mientras que la cuota de espacio determina la limitación en términos de gigabytes escritos, la cuota de ficheros determina la limitación en términos de número de ficheros escritos.

La cuota funciona en dos pasos, que se llaman soft quota y hard quota:

- **Soft quota**: Cuando excedes tu cuota, recibirás un mensaje de advertencia cada vez que inicies sesión en Picasso. En la figura siguiente, puedes ver un ejemplo de alguien que excede la softquota de espacio libre.
<div style="text-align:center">
<img src="Figuras/Cuota_7_dias.png" width="1000"/>
</div>

- **Hard quota**: Cuando excedes tu cuota por mucho, encontrarás un límite estricto que no te permitirá escribir más ficheros, incluso si estabas dentro del periodo de gracia de 7 días de la soft quota.

Una vez que se alcanza la cuota (de espacio o de ficheros), tienes 7 días para volver a la situación normal. Si pasan esos 7 días o se alcanza la hard quota, la escritura en disco se bloqueará.

Para verificar tus cuotas, puedes ejecutar el comando:
```
quota
```
o 
```
mmlsquota
```


### 2.3.3 - Sistema de ficheros de scratch rápido (FSCRATCH) y política de purga <a id="sec_2.3.3"></a>

**- Acerca de FSCRATCH**

El sistema de ficheros FSCRATCH (Fast Scratch) debe usarse para acelerar los trabajos, especialmente aquellos que hacen un uso intenso del almacenamiento. Este espacio está concebido como un sistema de ficheros pseudo-volátil. Esto significa que los datos almacenados aquí se eliminarán periódica y automáticamente, así que <span style="color: red"> no deberías usarlo para almacenar ficheros importantes.
</span>:

Para ir a FSCRATCH, escribe 

```
cd $FSCRATCH
```
Puedes copiar carpetas de HOME a FSCRATCH usando un comando como:
```
cp -r $HOME/path/to/your/folder/in/home $FSCRATCH/path/to/target/folder
```
o desde FSCRATCH a HOME usando
```
cp -r $FSCRATCH/path/to/your/folder/in/fscratch $HOME/path/to/target/folder
```

No olvides copiar los datos de salida importantes de vuelta a tu HOME, porque 
se eliminarán después de algunas semanas.

**- Política de purga**

Los ficheros que no se hayan utilizado durante más de dos meses se eliminarán automáticamente.

Los ficheros no se eliminarán después de exactamente dos meses, pero los ficheros que no se hayan utilizado durante dos meses estarán sujetos a
eliminación en cualquier momento sin previo aviso. La purga se activa en función del porcentaje de uso **total** de FSCRATCH.

Si no estás seguro de cómo usar FSCRATCH, por favor contáctanos a soporte@scbi.uma.es.


### 2.3.4 - Sistema de ficheros de scratch local <a id="sec_2.3.4"></a>

Hay algunos nodos que tienen un sistema de ficheros de scratch local llamado LOCALSCRATCH. Este scratch local es aún más rápido que el sistema de ficheros fscratch, pero tiene una desventaja principal: solo es accesible desde cada nodo, por lo que no puedes acceder a él desde la máquina donde inicias sesión, sino solo desde el script SBATCH que enviarás al sistema de cola (usando la variable de entorno $LOCALSCRATCH).

El scratch local es muy rápido y puede acelerar sustancialmente algunos trabajos cuando se utiliza. Y es imprescindible cuando un trabajo necesita escribir muchos ficheros o hacer un uso intensivo del disco. También puedes encontrar un ejemplo en la sección [Cómo enviar trabajos](#sec_4).

Si crees que necesitas acceso al scratch local y no estás seguro de cómo usarlo, por favor contáctanos a soporte@scbi.uma.es.

### 2.3.5 - Política de copias de seguridad <a id="sec_2.3.5"></a>

<span style="color: red"> NOTA IMPORTANTE </span>: Es importante que sigas una política de copias de seguridad responsable. No somos responsables de la pérdida de datos almacenados en nuestros sistemas, por lo que si tus datos son importantes, deberías tener copias de seguridad en tu propia máquina o sistema de copias de seguridad. Como cortesía, mantenemos una copia de seguridad de los ficheros almacenados en el directorio de inicio, pero no quedan garantizadas, ni podemos hacer copias de seguridad de todo el espacio disponible. Puedes seguir estas pautas de copias de seguridad si lo deseas:

- Es una buena práctica usar un sistema de control de versiones para tus propios programas y scripts. Git puede ser una buena solución (https://git-scm.com/). Los sistemas de control de versiones ayudan a los programadores a llevar un seguimiento de todos los cambios realizados en el código fuente, scripts, etc. Cada vez que realizas un cambio en un archivo, puedes guardarlo en tu sistema de control de versiones con alguna descripción textual, y luego puedes ver esos cambios en cualquier momento o retroceder a una versión anterior. Esto no es una copia de seguridad real, pero es una especie de ella.
- Mantén diferentes copias de seguridad, de diferentes fechas. Las copias de seguridad también son útiles si eliminas o modificas un archivo por error.
- Almacena las copias de seguridad en lugares físicos diferentes. De esta manera, si la ubicación principal de tu computadora sufre un desastre, podrías acceder a otra copia que tengas en otro lugar.
- Intenta acceder a tus datos de copia de seguridad periódicamente. Puedes hacer muchas copias de seguridad, pero si no son accesibles, no son útiles.


[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)

# 3 - Iniciar sesión en Picasso <a id="sec_3"></a>

Como la mayoría de los supercomputadores, Picasso se basa en una distribución de Linux, en este caso openSuse Leap 15.4. El acceso remoto al sistema se realiza mediante el protocolo SSH (puerto 22), conectándose a un servidor de inicio de sesión. En este servidor encontrarás todos los compiladores y herramientas necesarias para preparar y enviar tus trabajos al sistema de cola.

## 3.1 - Conexión SSH <a id="sec_3.1"></a>

Para conectarte al servidor de inicio de sesión, necesitarás ingresar el siguiente comando en la **terminal del sistema** (puede ser CMD o PowerShell en Windows, o la terminal de Linux y MacOs):
```
ssh <username>@picasso.scbi.uma.es
```
Por ejemplo, si tu nombre de usuario es *myuser*, deberías ingresar:

```
myuser@picasso.scbi.uma.es
```

Después de esto, se te pedirá que ingreses tu contraseña. Cuando la ingreses, verás que **no aparece nada en la** 
**pantalla**, pero se está registrando. Presiona enter cuando hayas terminado, y la conexión debería establecerse.

<span style="color: red">  Advertencia </span>: Si fallas al ingresar la contraseña varias veces, el sistema bloqueará 
tu IP. Se desbloqueará después de 30 minutos. Si vuelves a fallar varias veces, la IP será bloqueada permanentemente. 
Tendrás que contactarnos en soporte@scbi.uma.es para desbloquearla.

Consejo: si tienes problemas de sesión y tu conexión se interrumpe después de un corto tiempo de inactividad o debido a 
la estabilidad de la conexión a Internet; debes incluir un comando de mantener viva la conexión en tus conexiones:

```
ssh ServerAliveInterval=60 myuser@picasso.scbi.uma.es
```

## 3.2 - MobaXTerm <a id="sec_3.2"></a>

Si no estás familiarizado con las terminales, tal vez puedas probar a usar el programa <a href="https://mobaxterm.mobatek.net/" target="_blank">MobaXTerm</a>. Es más fácil de usar y permite cosas como copiar un archivo usando el ratón.

## 3.3 - Aviso importante <a id="sec_3.3"></a>

<span style="color: red"> NOTA IMPORTANTE </span>: Cuando accedes a Picasso, estás ingresando en uno de nuestros nodos, el **nodo de inicio de sesión**. El nodo de inicio de sesión no es un lugar para ejecutar tu trabajo. Puede ser utilizado para construir scripts, compilar programas, probar que un comando complejo que vas a utilizar en el script SBATCH se está ejecutando correctamente, etc., pero NO para realizar trabajo real. Todos los programas lanzados serán automáticamente detenidos sin previo aviso cuando utilicen más de 10 minutos de tiempo de CPU.

El trabajo real debe ser enviado al **sistema de cola** (ver sección [Cómo enviar trabajos](#sec_4)).

[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)

# 4 - Cómo enviar trabajos <a id="sec_4"></a>

Nuestro sistema de cola actual es **Slurm**. Entonces, cualquier <a href="https://slurm.schedmd.com/documentation.html" target="_blank">manual de Slurm</a> te dará información más detallada sobre estos comandos. Esta es solo una guía de inicio rápido:

## 4.1 - Preparación para enviar un trabajo  <a id="sec_4.1"></a>

Antes de enviar un trabajo al sistema de cola, solo tienes que escribir un pequeño archivo de script con un formato específico. Llamamos a este script **script SBATCH**. Aquí es donde se solicitan los recursos al sistema de cola y donde se colocan las sentencias de ejecución. Este script está escrito en lenguaje bash (el mismo que en la terminal).

En Picasso tenemos un comando para generar una plantilla para este tipo de scripts:
```
gen_sbatch_file script.sh "executing_command"
```
Este comando generará un script llamado "script.sh" con el comando "executing_command". Solo tienes que editar este archivo para ajustar los recursos que deseas solicitar, cargar los módulos y ajustar la declaración de ejecución. En la sección [Modificación de recursos y límites](#sec_4.2) veremos cómo hacerlo.

Cada software tiene su propia forma de llamarlo para resolver un trabajo, pero no te preocupes, ya que encontrarás todos los detalles en las instrucciones individuales, guías o ficheros readme de cada software.

## 4.2 - Modificación de recursos y límites <a id="sec_4.2"></a>

Aquí vamos a ver cómo modificar el script SBATCH de ejemplo generado con el comando:

```
gen_sbatch_file script.sh "executing_command"
```
Si ingresas a este archivo, verás algo como esto:

```
#!/usr/bin/env bash
# Leave only one comment symbol on selected options
# Those with two commets will be ignored:
# The name to show in queue lists for this job:
##SBATCH -J script_2.sh

# Number of desired cpus (can be in any node):
#SBATCH --ntasks=1

# Number of desired cpus (all in same node):
##SBATCH --cpus-per-task=1

# Amount of RAM needed for this job:
#SBATCH --mem=2gb

# The available nodes are:
#     AMD nodes with 128 cores and 1800GB of usable RAM
#     AMD nodes  with 128 cores and 439GB of usable RAM
#     Intel nodes with 52  cores and 187GB of usable RAM

# The time the job will be running:
#SBATCH --time=10:00:00

# If you need nodes with special features you can select a constraint.
# Please, use cal by default. You will be assigned a node that satisfies your requests.
#SBATCH --constraint=cal

# Change "cal" by "sd" if you want to use Intel nodes and by "sr" if you want to use AMD nodes.
##SBATCH --constraint=sd
##SBATCH --constraint=sr

# To use GPU, comment out the constraint line and uncomment the following line.
##SBATCH --gres=gpu:1

# Set output and error files
#SBATCH --error=job.%J.err
#SBATCH --output=job.%J.out

# Leave one comment in following line to make an array job. Then N jobs will be launched. In each one SLURM_ARRAY_TASK_ID will take one value from 1 to 100
##SBATCH --array=1-100

# To load some software (you can show the list with 'module avail'):
# module load software


# the program to execute with its parameters:
time executing_command
```

Primero que nada, debes saber que en bash todas las líneas que comienzan con "#" son **comentarios**. Como puedes ver, casi todas son comentarios. **Las sentencias para solicitar recursos al sistema de colas deben estar comentadas**. Deben comenzar con `#SBATCH`. Si comienza con dos o más '#', la sentencia será ignorada.

En el ejemplo anterior, las sentencias a tener en cuenta son las siguientes:

- `#SBATCH --ntasks=1`: &nbsp; Número de tareas (procesos). Si utilizas bibliotecas de paralelización como MPI, este número debería ser igual al número de tareas de MPI.
- `#SBATCH --mem=2gb`: &nbsp; Memoria RAM total solicitada. Si el trabajo intenta usar más de esta memoria, terminará con un error `out_of_memory`.
- `#SBATCH --time=10:00:00`: &nbsp; Tiempo total de ejecución. Cuando se agote este tiempo, el trabajo será cancelado.
- `#SBATCH --constraint=cal`: &nbsp; Esto es para seleccionar el tipo de nodos en los que deseas ejecutar el trabajo. "cal" significa cualquier nodo (excepto nodos GPU).
- `#SBATCH --error=job.%J.err`: &nbsp; Nombre del archivo donde se guardarán los mensajes de error de la ejecución del programa (%J será reemplazado por el id del trabajo).
- `#SBATCH --output=job.%J.out`: &nbsp; Nombre del archivo donde se guardarán los mensajes de salida de la ejecución del programa (%J será reemplazado por el id del trabajo).

En el ejemplo anterior se han incluido algunas declaraciones '##' que serán ignoradas. Se incluyen por si acaso son necesarias, se pueden descomentar. Estas sentencias son:

- `##SBATCH -J script_2.sh`: &nbsp; Esto es para cambiar el nombre bajo el cual aparecerá el trabajo en la cola. Por defecto, se le asigna el mismo nombre que el script SBATCH.
- `##SBATCH --cpus-per-task=1`: &nbsp; Esto es para cambiar el número de CPUs solicitadas por cada tarea. Por defecto se asigna 1 CPU por tarea.
- `##SBATCH --constraint=sd`: &nbsp; Esto es para que el trabajo solo pueda ingresar a los nodos sd (Intel).
- `##SBATCH --constraint=sr`: &nbsp; Esto es para que el trabajo solo pueda ingresar a los nodos sr (AMD).
- `##SBATCH --constraint=bc`: &nbsp; Esto es para que el trabajo solo pueda ingresar a los nodos bc (AMD).
- `##SBATCH --gres=gpu:1`: &nbsp; Esto es para solicitar GPUs. Primero, las declaraciones deben estar comentadas con "--constraint". El número al final se refiere a cuántas GPUs se están solicitando.
- `##SBATCH --array=1-100`: &nbsp; Esto es para usar trabajos de array. Se explicará en la sección [Array jobs: how to send lots of jobs](#sec_4.6)

<span style="color: red">  NOTAS IMPORTANTES: </span>

- Todas las comandos #SBATCH deben ir al inicio del archivo, sin líneas comentadas encima de ellas, porque cualquier línea SBATCH después de la primera línea sin comentar será ignorada por slurm.
- Los límites de recursos tienen políticas estrictas. Significa que, si excedes los recursos solicitados, tu trabajo será finalizado.
- Puedes evaluar los recursos que un trabajo ha utilizado efectivamente ejecutando ``seff id_trabajo`` cuando ya haya finalizado (`seff` no funciona si el trabajo está en ejecución). Esto te permitirá ajustar los recursos para una utilización óptima (tus trabajos comenzarán a resolverse más pronto). También puedes usar el nuevo <a href="https://www.scbi.uma.es/slurm_monitor/admin?locale=es" target="_blank">monitor de trabajos en línea</a> para esta tarea. En la sección [Monitoring queued jobs](#sec_4.7), puedes encontrar más detalles al respecto.

<span style="color: Purple">  Para usuarios antiguos: </span> La nueva versión de Slurm ha cambiado el comando --cpus por --cpus-per-task. Debes actualizar tus scripts para obtener los recursos solicitados.

## 4.3 - Solicitar GPUs <a id="sec_4.3"></a>

Como se discutió brevemente en la sección anterior, para solicitar GPUs, las líneas "--constrain" deben estar comentadas (con dos '##'):

```
##SBATCH --constraint=cal
```
y la línea

```
#SBATCH --gres=gpu:1
```
Debe estar sin comentar (solo un '#'). Si desea utilizar más de una GPU, simplemente cambie el "1" por otro número.
Recuerde que nuestros nodos exa tienen 8 GPUs cada uno.

## 4.4 - Generador de trabajos de muestra <a id="sec_4.4"></a>

También hemos creado una herramienta que genera un trabajo de muestra completo para algunos programas. Puede ver una lista de trabajos de muestra disponibles con este comando:

```
gen_sample_job | grep -v NO
```
Cuando haya localizado el trabajo de muestra deseado, puede generarlo con el siguiente comando:
```
gen_sample_job <sofware> <output_foler>
```
Donde `<software>` es el software deseado sin la versión, y `<carpeta_salida>` es la carpeta que se creará
para contener el script sh y otros ficheros necesarios. Por ejemplo, si desea crear un trabajo de muestra para el software
Gaussian en una nueva carpeta llamada gaussian_job, debería ingresar:

```
gen_sample_job gaussian gaussian_job
```
<span style="color: red">  Nota: </span> No tenemos muchos ejemplos y la mayoría de ellos pueden ser antiguos.

## 4.5 - Envío de un trabajo <a id="sec_4.5"></a>

Cuando tenga una versión modificada del archivo script.sh adaptado a sus necesidades, estará listo para enviarlo al sistema de colas.
Para hacerlo, simplemente debe ingresar:

```
sbatch script.sh
```
Ahora, el trabajo ha sido recibido por el sistema de colas, que buscará los recursos solicitados. Una vez que los recursos estén disponibles,
el trabajo comenzará.

En la sección "Monitoreo de trabajos en cola" aprenderá cómo monitorear el estado de sus trabajos. De esta manera, sabrá si
el trabajo todavía está buscando un lugar para ser ejecutado (en cola) o si ya está en ejecución.


<span style="color: red">  Nota importante: </span> Notará que si solicitó recursos adaptados a sus necesidades
(y no en exceso), su trabajo comenzará mucho más rápido, ya que encontrará un lugar para ser ejecutado mucho más fácilmente. También tenga en
cuenta que si solicita menos recursos de los que necesitará su trabajo, el trabajo será eliminado inmediatamente tan pronto como
los recursos sean superados por el software.



## 4.6 - Trabajos en array: cómo enviar muchos trabajos <a id="sec_4.6"></a>

Cuando necesitas enviar un conjunto de trabajos que ejecuten el mismo comando sobre diferentes datos, puedes hacer uso de los trabajos en array. Los trabajos en array son ahora una opción nativa de Slurm, por lo que encontrarás información avanzada sobre ellos en el [manual de Slurm](https://slurm.schedmd.com/documentation.html).

Para usar trabajos en array, solo necesitas hacer algunos cambios en el archivo de script. En primer lugar, elimina un símbolo de comentario de la línea `--array` (dejándolo solo con un símbolo de comentario '#'):

```
# Deje un comentario en la siguiente línea para hacer un trabajo en array. Luego se lanzarán N trabajos. En cada uno SLURM_ARRAY_TASK_ID tomará un valor de 1 a 100
#SBATCH --array=1-100
```
De esta manera, Slurm enviará 100 trabajos, con la única diferencia de que la variable de entorno `SLURM_ARRAY_TASK_ID` variará de 1 a 100. Una forma de utilizarlo para pasar diferentes ficheros de datos al programa para cada ejecución es nombrar los ficheros en forma de "data_0, data_1,..., data_100" y llamar al programa de la siguiente manera:


```
time my_command data_${SLURM_ARRAY_TASK_ID}
```


También puedes elegir algunos valores específicos para esta variable, por ejemplo `7,55,87,95,4,2`:


```
#SBATCH --array=7,55,87,95,4,2
```


Después de estas modificaciones, debes enviarlo al sistema de cola, usando el comando sbatch normal:


```
sbatch script.sh
```


<span style="color: Red">  Nota: Si vas a enviar un trabajo en array de más de 1000 trabajos por primera vez, por favor, contáctanos primero. </span>

## 4.7 - Monitoreo de trabajos en cola <a id="sec_4.7"></a>

### 4.7.1 - Comando squeue <a id="sec_4.7.1"></a>

En cualquier momento, puedes monitorear la cola de trabajos ejecutando este comando:


```
squeue
```

Por defecto, squeue muestra trabajos en formato corto (agrupando trabajos en array juntos). Si necesitas acceder al formato largo, utiliza el indicador `-l`:


```
squeue -l
```


### 4.7.2 - Nuevo monitor de trabajos en línea <a id="sec_4.7.2"></a>

Para obtener información más detallada sobre tus trabajos en ejecución, puedes acceder al nuevo monitor de trabajos en línea. Esta utilidad te mostrará detalles en tiempo real sobre el número de CPU y la cantidad de RAM utilizada, y también el uso de GPU y VRAM si corresponde. Para usar el monitor en línea, sigue estas instrucciones:

1. Ingresa a https://www.scbi.uma.es/slurm_monitor/admin/login
2. Inicia sesión con tus credenciales de usuario de picasso
3. Verás una lista de todos tus trabajos en ejecución o finalizados
4. Usando los controles de la primera fila, puedes ordenar los trabajos por cualquier columna
5. Al utilizar los filtros a la derecha, solo se mostrarán los trabajos que te interesen
6. Haz clic en el trabajo deseado
7. Verás más detalles en la parte superior y gráficos en tiempo real debajo
8. Al hacer clic en los diferentes elementos de la leyenda, puedes ocultar o mostrar su gráfico correspondiente
    - Sistema: Puede ser un indicador del uso de disco. Si es alto, deberías usar localscratch
    - Nuevo proc: Una línea vertical aparecerá cada vez que se detecte un nuevo proceso. Es útil cuando usas varios programas en tu script.
    - Cores reservados: Línea horizontal con los núcleos que se solicitaron.
    - RAM reservada: Línea horizontal con los GB de RAM que se solicitaron.
    - RAM: RAM realmente utilizada.
    - Cores: Núcleos de CPU realmente utilizados.

Recuerda que si ajustas tus recursos solicitados a los que realmente puedes usar, tu trabajo comenzará a resolverse más rápido, ya que encontrará más rápido un lugar para ser ejecutado. Además, más recursos estarán disponibles para otros usuarios en picasso.



## 4.8 - Cancelación de trabajos <a id="sec_4.8"></a>

En ocasiones, querrás cancelar un trabajo que ya está en ejecución o en cola. Para hacerlo, solo tienes que tomar el número de identificación del trabajo (primera columna mostrada en squeue) y emitir este comando:


```
scancel <JOBID>
```
donde `<ID_DE_TRABAJO>` es el número del trabajo que se cancelará.

Para cancelar solo algunos trabajos de un trabajo en array, utiliza este formato:


```
scancel <JOBID>_[1-50]
```
En ese ejemplo, habrías cancelado los trabajos del 1 al 50 del trabajo en array con ID ID_DE_TRABAJO.


## 4.9 - Uso del sistema de ficheros LOCALSCRATCH <a id="sec_4.9"></a>

Por defecto, puedes trabajar y crear ficheros temporales en tu sistema de ficheros $FSCRATCH normal, pero a veces puede que necesites usar un programa que genere miles y miles de ficheros temporales muy rápido. Eso no es un comportamiento adecuado para sistemas de ficheros compartidos, ya que cada creación de archivo pequeño realiza algunas solicitudes al almacenamiento compartido para completarse. Si hay miles de ellos, pueden congestionar el sistema en algún momento.

En estos casos extremos, es obligatorio utilizar el sistema de ficheros $LOCALSCRATCH. En situaciones menos extremas, en las que el software ejecuta operaciones de E/S grandes, también puedes aprovechar la aceleración que proporciona el sistema de ficheros Localscratch. Como se ha visto en la sección de hardware, todas las máquinas tienen al menos 900GB de localscratch. **Para un uso alto de localscratch, por favor, contáctanos primero.**

El sistema de ficheros localscratch es independiente para cada nodo, y por lo tanto, no se comparte entre nodos y no es accesible desde las máquinas de inicio de sesión. Debido a eso, debes entender cómo copiar tus datos allí, usarlos y luego recuperar los resultados importantes de vuelta a tu directorio de inicio (todo hecho dentro del script sbatch). Aquí puedes encontrar un ejemplo que podría ayudarte en estas tareas. No dudes en contactarnos si tienes alguna pregunta.


```
#!/usr/bin/env bash
# Leave only one comment symbol on selected options
# Those with two commets will be ignored:
# The name to show in queue lists for this job:
##SBATCH -J script_2.sh

# Number of desired cpus (can be in any node):
#SBATCH --ntasks=1

# Number of desired cpus (all in same node):
##SBATCH --cpus-per-task=1

# Amount of RAM needed for this job:
#SBATCH --mem=2gb

# The available nodes are:
#     AMD nodes with 256 cores and 683GB of usable RAM
#     AMD nodes with 128 cores and 1800GB of usable RAM
#     AMD nodes  with 128 cores and 439GB of usable RAM
#     Intel nodes with 52  cores and 187GB of usable RAM

# The time the job will be running:
#SBATCH --time=10:00:00

# If you need nodes with special features you can select a constraint.
# Please, use cal by default. You will be assigned a node that satisfies your requests.
#SBATCH --constraint=cal

# Change "cal" by "sd" if you want to use Intel nodes and by "sr" if you want to use AMD nodes.
##SBATCH --constraint=sd
##SBATCH --constraint=sr

# To use GPU, comment out the constraint line and uncomment the following line.
##SBATCH --gres=gpu:1

# Set output and error files
#SBATCH --error=job.%J.err
#SBATCH --output=job.%J.out

# Leave one comment in following line to make an array job. Then N jobs will be launched. In each one SLURM_ARRAY_TASK_ID will take one value from 1 to 100
##SBATCH --array=1-100

# To load some software (you can show the list with 'module avail'):
# module load software

# create a temp dir in localscratch
MYLOCALSCRATCH=$LOCALSCRATCH/$USER/$SLURM_JOB_ID
mkdir -p $MYLOCALSCRATCH

# execute there the program
cd $MYLOCALSCRATCH
time program1 $HOME/data/data1 > results

#copy some results back to home
cp -rp your_results $HOME/place_to_store_results

#remove your localscratch files:

if cd $LOCALSCRATCH/$USER; then
if [ -z "$MYLOCALSCRATCH" ]; then
rm -rf --one-file-system $MYLOCALSCRATCH
fi
fi
```



[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)


# 5 - Copiar ficheros desde/hacia picasso <a id="sec_5"></a>

En algún momento necesitarás copiar ficheros desde o hacia picasso. Tenemos que diferenciar dos casos:


## 5.1 - Descarga de ficheros desde internet <a id="sec_5.1"></a>

En caso de que quieras **descargar** un archivo en picasso desde una URL disponible en **internet**, puedes hacerlo usando el comando wget en la consola de picasso:

```
wget <url>
```
Por ejemplo, para descargar un archivo desde la URL https://www.example.com/file.txt, debes usar:

```
wget https://www.example.com/file.txt
```
Es común que el comando wget <url> no funcione cuando el archivo que necesitas descargar requiere que ingreses una contraseña, que inicies sesión en alguna cuenta, o que realices alguna otra acción antes de descargar. En estos casos, necesitarás instalar un complemento para tu navegador web. Este complemento generará el comando wget completo y funcionando para ti. Luego solo tendrás que pegar el comando en picasso y esperar a que la descarga termine. Estos son los pasos que debes seguir:

1. Descarga e instala uno de estos complementos según el navegador web que uses (<a href="https://chrome.google.com/webstore/detail/curlwget/dgcfkhmmpcmkikfmonjcalnjcmjcjjdn" target="_blank">curlwget</a> para Chrome, <a href="https://addons.mozilla.org/es/firefox/addon/cliget/" target="_blank">cliget</a> para Firefox, <a href="https://microsoftedge.microsoft.com/addons/detail/curlwget/njimejjehbbfhipbgakbleoobdgdcmof" target="_blank">curlwget</a> para Edge).
2. Inicia la descarga (en tu computadora) del archivo que te interesa, luego detén la descarga.
3. Ahora haz clic en el icono del complemento (generalmente en la esquina superior derecha de tu navegador web).
4. Debería aparecer el comando wget completo. Copia el comando wget completo.
5. Pégalo en picasso y presiona Enter. La descarga debería comenzar.





## 5.2 - Copiando ficheros desde y hacia picasso <a id="sec_5.2"></a>

### 5.2.1 - Comando scp <a id="sec_5.2.1"></a>

En caso de que necesites *copiar* un archivo desde/hacia picasso a/desde tu computadora, puedes usar el comando 

```
scp -r <from_path_file> <to_destination_path>
```
Este comando se puede utilizar para copiar en ambas direcciones.

**Para copiar desde picasso a tu computadora:**

```
scp -r <user>@picasso.scbi.uma.es:<file_path_in_picasso> <file_local_destination>
```
Puedes obtener la ruta de una carpeta en Picasso usando el comando 

```
pwd
```
Debes moverte a la carpeta que deseas copiar y ejecutar este comando.

**Para copiar desde tu computadora a picasso:**

```
scp <file_local_destination> <user>@picasso.scbi.uma.es:<file_destination_in_picasso>
```
Para obtener su ruta local en tu computadora, simplemente haz clic en la barra superior del explorador de ficheros y copia la ruta, como puedes ver en la figura 
<div style="text-align:center">
<img src="Figuras/File_explorer.png" width="1000"/>
</div>

### 5.2.2 - Comando rsync <a id="sec_5.2.2"></a>

Si deseas copiar muchos ficheros, recomendamos el uso del comando rsync, es muy similar a scp, pero rsync puede 
omitir ficheros ya transferidos, por lo que realiza una sincronización en lugar de una copia completa. La sintaxis es muy similar.

**Para copiar desde picasso a tu computadora:**

```
rsync -CazvHu <user>@picasso.scbi.uma.es:<file_path_in_picasso> <file_local_destination>
```
**Para copiar desde tu computadora a picasso:**

```
rsync -CazvHu <file_local_destination> <user>@picasso.scbi.uma.es:<file_destination_in_picasso>
```
<span style="color: red">  NOTA </span>: Para transferencias pesadas, recomendamos usar el comando rsync, ya que si la transferencia 
se interrumpe por cualquier motivo, omitirá los ficheros existentes cuando intentes cargarlos nuevamente.




[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)

# 6 - Software <a id="sec_6"></a>

## 6.1 - Software disponible <a id="sec_6.1"></a>

Tenemos una amplia variedad de software instalado y listo para usar. Puedes consultar la lista actualizada en nuestra 
<a href="https://www.scbi.uma.es/site/scbi/software" target="_blank">página web</a>
(puede estar desactualizada), o ejecutando el siguiente comando en el servidor de inicio de sesión (recomendado):

```
module avail
```
Para buscar un software específico
```
module avail | grep -i software_name
```
Por ejemplo, para buscar instalaciones de un software como WRF (Weather Research and Forecasting), puedes usar el comando
```
module avail | grep -i wrf
```


## 6.2 - Cómo cargar/descargar software <a id="sec_6.2"></a>

### 6.2.1 - Cargar un software <a id="sec_6.2.1"></a>

Para cargar un módulo solo tienes que ejecutar el comando

```
module load software_name
```
Puedes obtener los nombres de los software con los comandos de la sección anterior.

Por ejemplo, si deseas cargar la versión 4.4.2 compilada de WRF compilada con intel, debes escribir

```
module load WRF/4.4.2_intel_mpi
```
Debes incluir el comando de carga del módulo en tu script SBATCH.

También funciona si ejecutas el `module load` en la terminal antes de enviar el trabajo al sistema de encolado, pero no 
se recomienda debido a su tediosidad. Esto se debe a que cada vez que accedes a Picasso inicias una sesión "limpia" 
(sin ningún módulo cargado), por lo que tendrías que cargar los módulos cada vez que ingreses a Picasso.

Si deseas ejecutar comandos directamente en la terminal (como abrir un intérprete de una de nuestras versiones de Python), 
deberás cargar el módulo ejecutándolo en la terminal.

### 6.2.2 - Listar el software cargado <a id="sec_6.2.2"></a>

Para ver los paquetes que has cargado previamente:

```
module list
```


### 6.2.3 - Descargar software <a id="sec_6.2.3"></a>

Para descargar cualquier paquete previamente cargado:

```
module unload software_name
```
Por ejemplo, si deseas descargar el WRF previamente cargado:
```
module unload WRF/4.4.2_intel_mpi
```
También puedes usar el siguiente comando para descargar todo el software que hayas cargado. (Nota: si te desconectas 
de picasso, todo el software se descarga automáticamente).

```
module purge
```

## 6.3 - Compilación de software <a id="sec_6.3"></a>

Para compilar tu propio software, puedes usar diferentes compiladores (gcc, intel, pgi, ...). Cada software tiene sus 
propias instrucciones de compilación, pero normalmente puedes compilarlo con diferentes compiladores.

Gcc es el predeterminado, pero el compilador de Intel puede acelerar tu código. Para compilar usando el compilador de 
Intel, primero debes cargarlo:

```
module load intel/2024.0.1
```


# 7 - Comandos propios de Picasso <a id="sec_7"></a>

Desde el equipo de soporte de Picasso, hemos desarrollado una serie de comandos para ayudar a los usuarios. Estos son los 
siguientes:

- `count_files`: Este comando devolverá el número de ficheros dentro de las carpetas del directorio actual.
- `free_gpus.sh`: Este comando te mostrará las GPU disponibles.
- `resource_efficiency`: Este comando genera el gráfico que puedes ver cuando ingresas a Picasso. Te muestra el 
porcentaje de CPU y RAM utilizados con respecto al total solicitado para los últimos 5 trabajos que se han completado 
**exitosamente**. También puedes generar el gráfico para los trabajos que desees pasando los identificadores de los 
trabajos al comando:
    ```
    resource_efficiency job_id job_id job_id job_id job_id
    ```
    También puedes ver el mensaje de ayuda con 
    ```
    resource_efficiency -h 
    ```




[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)

# 8 - Preguntas frecuentes <a id="sec_8"></a>

Esta sección contiene respuestas a preguntas frecuentes:

## 8.1 - ¿Cuántos recursos debo solicitar para mis trabajos? <a id="sec_8.1"></a>

Es importante ajustar los recursos a tus necesidades. Demasiados pocos recursos resultarán en trabajos cancelados, y demasiados recursos aumentarán el tiempo que tu trabajo necesita para encontrar un lugar donde ejecutarse, también resultando en menos recursos libres para otros usuarios.

Puedes utilizar el <a href="https://www.scbi.uma.es/slurm_monitor/admin?locale=es" target="_blank">monitor de trabajos en línea</a> (explicado en la subsección "[Monitoreo de trabajos en cola](#sec_4.7)") para evaluar si estás utilizando los recursos correctamente. También es útil el comando seff id_del_trabajo, una vez el trabajo ha terminado.

Incluso si estás utilizando todos los núcleos que solicitaste, no tiene que significar que se estén utilizando correctamente. Algunos programas no escalan bien.

Como ejemplo, hay programas que usando 64 núcleos resuelven los problemas casi el doble de rápido que cuando se usan 32 núcleos. Sin embargo, otros programas no son tan buenos, y solo pueden mejorar la velocidad en un 10% en tal escenario, o incluso durar más con 64 núcleos que con 32.

Si experimentas este tipo de problema, o si necesitas ayuda para ajustar los recursos, prepara un ejemplo de trabajo que dure aproximadamente 2 horas para finalizar y contáctanos en `soporte@scbi.uma.es`.

## 8.2 - Mensaje de error: Conetion refused/The network is not available <a id="sec_8.2"></a>

Si recibes este mensaje de error, tu IP ha sido bloqueada debido a demasiados intentos de inicio de sesión fallidos. Si no has sido desbloqueado automáticamente en 30 minutos, contáctanos en `soporte@scbi.uma.es`.

## 8.3 - Mensaje de error: Remote host identification has changed <a id="sec_8.3"></a>

Si ves un mensaje con alguno de estos textos: "Remote host identification has changed"; "Es posible que alguien esté haciendo algo malo". Puede ser por varias violaciones de seguridad pero, hemos cambiado nuestra huella digital recientemente (julio de 2021). Si no has conectado desde esta fecha, debes eliminar la clave antigua y usar la nueva. Para hacer esto, por favor lee el mensaje de advertencia completo y identificarás un texto que dice "Puedes usar el siguiente comando para eliminar la clave ofensiva:". Después de eso, se muestra un comando que debes ejecutar con tu ruta personal a las claves SSH. En un sistema Linux será pre-asumiblemente como:


```
ssh-keygen -R picasso.scbi.uma.es -f <yourPath>
```



## 8.4 - ¿Cómo cambio mi contraseña? <a id="sec_8.4"></a>

Si ya conoces tu contraseña y deseas cambiarla, puedes hacerlo usando el comando:

```
passwd
```
Te pedirá tu contraseña actual. Luego, se te pedirá dos veces la nueva contraseña y, eventualmente, se mostrará un mensaje de cambio exitoso.

## 8.5 - ¿Por qué se cancela mi proceso en el nodo de inicio de sesión? <a id="sec_8.5"></a>

La máquina de inicio de sesión no es un lugar para ejecutar tu trabajo. Puede usarse para construir scripts, compilar programas, probar que un comando complejo que vas a usar en el script SBATCH se está lanzando correctamente, etc., pero NO para realizar un trabajo real. Todos los programas lanzados se eliminarán automáticamente sin previo aviso cuando utilicen más de 10 minutos de tiempo de CPU.

## 8.6 - ¿Por qué mi trabajo está en cola durante tanto tiempo? <a id="sec_8.6"></a>

Probablemente se deba a que los recursos que solicitaste son excesivos. Notarás que si solicitaste recursos adaptados a tus necesidades (y no en exceso), tu trabajo comenzará mucho más rápido, ya que encontrará un lugar para ejecutarse mucho más fácilmente. También ten en cuenta que si solicitas menos recursos de los que necesitará tu trabajo, el trabajo se cancelará inmediatamente tan pronto como los recursos sean excedidos por el software.

Si pediste GPUs para tu trabajo, puedes verificar las GPUs disponibles actualmente ejecutando:

```
free_gpus.sh
```


## 8.7 - ¿Por qué mi trabajo no obtiene los recursos que solicité? <a id="sec_8.7"></a>

Todas las líneas de programas SBATCH (por ejemplo, #SBATCH --ntasks=8) deben ir al principio del archivo, sin líneas sin comentar encima de ellas, porque cualquier línea SBATCH después de la primera línea sin comentar será ignorada por slurm. Probablemente esto haya sucedido en tu archivo sbatch.

## 8.8 - Necesito más tiempo para mi trabajo <a id="sec_8.8"></a>

Los usuarios tienen un límite de tiempo de 3 o 7 días como máximo para el tiempo máximo de trabajo. Pedir más de 3 días es arriesgado, dado que la posibilidad de cualquier tipo de error aumenta con el tiempo.

Si incluso con 7 días no es suficiente para tu trabajo, claramente necesita alguna optimización (paralelismo, división, cambio de software, replanteamiento general, etc.). Puedes contactarnos en `soporte@scbi.uma.es` si necesitas ayuda para esta tarea.

## 8.9 - ¿Por qué ha fallado mi trabajo? <a id="sec_8.9"></a>

Puedes echar un vistazo a los ficheros de registro de errores y salida para obtener pistas sobre lo que sucedió.
El error "Command not found" se muestra cuando picasso no puede encontrar el comando que intentas ejecutar. Comúnmente se debe a olvidar incluir un comando de carga de módulo antes de la llamada al software correspondiente.

## 8.10 - Mensaje de error: cnf <comando> <a id="sec_8.10"></a>

Si tu trabajo intentó usar más recursos de los que solicitaste, el trabajo se cancelará automáticamente. En el caso de que estuviera saturando el sistema de una manera que interfiera con los trabajos de otros usuarios o si los recursos reservados para él se subutilizaran dramáticamente, lo cancelaremos manualmente.

## 8.11 - ¿Por qué se ha cancelado mi trabajo? <a id="sec_8.11"></a>

Si tu trabajo intentó usar más recursos de los que solicitaste, el trabajo se cancelará automáticamente. En el caso de que estuviera saturando el sistema de una manera que interfiera con los trabajos de otros usuarios o si los recursos reservados para él se subutilizaran dramáticamente, lo cancelaremos manualmente.

## 8.12 - Mensaje de error: Controlador de falta de memoria <a id="sec_8.12"></a>

Si tu trabajo intentó usar más RAM de la que solicitaste, el trabajo se cancelará automáticamente. Por favor, aumenta la cantidad de RAM solicitada en tu archivo sbatch y confirma que sigue la estructura #SBATCH `--mem=2gb`

## 8.13 - ¿Por qué no puedo editar ni crear nuevos ficheros? <a id="sec_8.13"></a>

Probablemente hayas excedido la cuota. Usa el comando 

```
quota
``` 
para comprobarlo. Recuerda que puedes alcanzar tanto la cuota suave como la dura debido al número de ficheros escritos o al tamaño de estos ficheros. Cuando hayas eliminado suficientes ficheros, podrás volver a crear y editar ficheros. Para obtener más información, consulta la sección "[Sistema de ficheros](#sec_2.3)".

Si no excediste tu cuota, entonces es posible que estés intentando escribir en una carpeta o editar un archivo en el que no tienes permiso de escritura.


## 8.14 - Necesito más espacio o cuota de ficheros <a id="sec_8.14"></a>

Recuerda que tienes dos ubicaciones separadas para tus ficheros, el $HOME (donde deberías almacenar los datos de entrada, tus propios scripts desarrollados, resultados finales y otros datos importantes) y el $FSCRATCH (donde deberías ejecutar tu trabajo).

Verifica que no conservas ningún archivo antiguo no deseado y elimínalos si los hay. Si necesitas aumentar la cuota debido a algún paquete conda / python, debes saber que no tienes que instalar el entorno completo en tu usuario. Es suficiente con ejecutar `module load anaconda` y luego `pip install` solo para el resto de los paquetes que no están en el módulo.

Si ninguno de los anteriores te ayuda, puedes contactarnos en `soporte@scbi.uma.es`.
