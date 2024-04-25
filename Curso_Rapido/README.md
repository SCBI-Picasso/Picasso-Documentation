# Curso rápido de introducción a Picasso

Autores:
- *Rafael Larrosa Jiménez (Administrador de Sistemas - SCBI)* 
- *David Castaño Bandín (Administrador de Sistemas - SCBI)*
- *Manuel Guerrero Claro (Administrador de Sistemas - SCBI)*

Para cualquier duda, contactar con soporte@scbi.uma.es

Video explicativos sobre el curso [aquí](https://www.scbi.uma.es/web/rafael/curso_rapido_picasso_ok.mp4)

**Añadir logos**

## Índice

- **[1 - Introducción](#sec_Intro)**
- **[2 - Acceso](#sec_acceso)**
- **[3 - Movimiento de ficheros](#sec_movimiento_ficheros)**
- **[4 - Recursos hardware](#sec_recursos_hardware)**
- **[5 - Sistema de ficheros / cuota](#sec_sistema_ficheros)**
- **[6 - Software](#sec_software)**
- **[7 - Sistema de colas](#sec_Sistema_de_colas)**
- **[8 - Array jobs](#sec_array_jobs)**
- **[9 - Selección de recursos](#sec_seleccion_de_recursos)**
- **[10 - Usando GPUs](#sec_usando_GPUs)**

<a id='sec_Intro'></a>
## 1. Introducción

En España hay una serie de infraestructuras públicas denominadas **ICTS (Infraestructuras Ciantifico Técnicas Singulares)**. El objetivo de estas es proveer a los investigadores españoles de  medios competitivos para llevar a cabo investigaciones de vanguardia. 

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/mapa_ICTS.jpg" align=center width='800px'/>
<center>Mapa de las ICTS en España.</center>
</center></figure>

Un ejemplo muy conocido de este tipo de infraestructuras son los famosos telescopios y observatorios astronómicos situados en Canarias. Si nos centramos más en el ámbito andaluz, tenemos la *Reserva Biológica de Doñana*, el *Observatorio Astronómico de Calor Alto* o la que nos compete en este curso: la **Red Española de Supercomputación (RES)** a traves del nodo **Picasso**.

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/mapa_RES.png" align=center width='800px'/>
<center>Mapa de las Red Española de Supercomputación (RES).</center>
</center></figure>

La RES está conformada por una serie de "nodos", es decir, una serie de **centros de supercomputación** repartidos por toda España. El SCBI con su supercomputador Picasso, con sus 40.000 núcleos, se situa como el **segundo nodo más potente de RES**, solo superado por el ampliamente conocido Marenostrum, situado en el BSC (Barcelona Supercomputer Center).

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/RES_grafica.png" align=center width='800px'/>
<center>Gráfica de la potencia de los diferentes nodos de la RES.</center>
</center></figure>

El SCBI también está inmerso en Computación Cuántica a través del proyecto QuantumSpain.

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/Quantum.png" align=center width='800px'/>
</center></figure>




<a id='sec_acceso'></a>
## 2. Acceso

El acceso a Picasso de sa usando el protocolo ssh en linea de comando:
```
ssh -X <user>@picasso.scbi.uma.es
```
Donde `<user>` debe de sustituirse por el usuario correspondiente. Este comando se puede ejecutar en:
- Un terminal de Linux
- Un terminal de MacOs
- Un PowerShell en Windows



<div class=\"alert alert-block alert-danger\">
<b>Nota</b>: 
Al escribir la contraseña no aparecerá nada en pantalla. Puede desconcertar al principio pero no preocuparse, se está escribiendo igual.
</div>


Otra opción sería usar un software dedicado a las conexiones ssh con servidores, como puede ser [MobaXterm](https://mobaxterm.mobatek.net/) o similares. MobaXterm es una buena opción para principiantes que no estén acostumbrados a manejar un terminal, pues este presenta un explorador de ficheros (columana de la izquierda), lo que facilita el moverse entre carpetas y mover archivos entre Picasso y el ordenador local 

<a id='mobaXterm-ssh.png'></a>
<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/mobaXterm-ssh.png" align=center width='800px'/>
</center></figure>


<div class=\"alert alert-block alert-danger\">
<b>Nota</b>    

Puedes encontrar una Demo sobre como conectarse con un servidor usando MobaXTerm [aquí](https://mobaxterm.mobatek.net/demo.html)
</div>

<a id='sec_movimiento_ficheros'></a>
## 3. Movimiento de ficheros

Para copiar ficheros entre Picasso y el ordenador local tenemos dos opciones:
- Usar comandos como **rsync** o **scp** en terminal
- Usar programas externos para abrir un explorador de archivos en Picasso (MobaXTerm, Dolphin en Linux, ...)

### 3.1. Los comandos scp y rsync

Lo primero que hay que tener en cuenta es que tanto los comandos de copiar desde el ordenador local a Picaso, como de Picasso al ordenador local, **se ejecutan en el ordenador local**. Ambos comandos sirven para mover archivos entre un ordenador local y un servidor, siendo más potente y versatil el comando rsync. Se recomienda el uso de rsync si lidiamos con grandes ficheros o grandes cantidades de archivos, pues el comando rsync es capaz de reanudar el copiado en caso de que se interrumpa.

#### Del ordenador local a Picasso

Lo primero que debemos hacer es habrir un teminal/PowerShell en la carpeta que contenga los ficheros y directorio que queramos copiar. Después, solo tenemos que ejecutar uno de los siguientes comandos
```
scp -r <file> <user>@picasso.scbi.uma.es:<destination>
rsync -CazvHu <file> <user>@picasso.scbi.uma.es:<destination>
```
donde 
- `<file>` debe de sustituirse por el nombre el archivo o carpeta que se quiere copiar
- `<user>` debe de sustituirse por el usuario de Picasso
- `<destination>`: debe de sustituirse con la ruta a la carpeta de destino en Picasso (Puede obtenerse usando el comando `pwd` en Picasso)


<div class=\"alert alert-block alert-danger\">
<b>Nota</b>: 
En Windows podemos abrir un PowerShell en una carpeta si dentro de ella pulsamos `Shift + Boton derecho del ratón`. De esta forma se desplegará un menú con opciones adiciones, entre ellas la de *Abrir un power shell aquí*.
<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/Abrir_powershell.jpeg" align=center width='800px'/>
<center>Abrir un PowerShell en una carpeta en Windows</center>
</center></figure>
</div>

#### De Picasso al ordenador local

Lo primero que debemos hacer es habrir un teminal/PowerShell en la carpeta donde queramos copiar los archivos provenientes de Picasso. Después, solo tenemos que ejecutar uno de los siguientes comandos
```
scp -r <user>@picasso.scbi.uma.es:<file> .
rsync -CazvHu <user>@picasso.scbi.uma.es:<file> .
```
donde 
- `<file>` debe de sustituirse por el nombre el archivo o carpeta que se quiere copiar
- `<user>` debe de sustituirse por el usuario de Picasso
- Fijemonos que hay un `.` al final del comando. Es importante ponerlo!!! (Es la ruta de destino. El punto significa "aquí")




### 3.2. Mover ficheros con MobaXTerm

Como ya comentamos antes, en la columna de la izquierda de MobaXTerm podemos mover ficheros entre Picasso y el ordenador local (ver [la Fig. anterior](#mobaXterm-ssh.png)). Esto puede hacerse simplemente arrastrando los ficheros o usando las opciones de cargar y descargar ficheros del menú de encima.

### 3.3. Otras alternativas 

Hay una gran variedad de softwares que permiten montar un servidor por sftp. Por ejemplo, las distribuciones de Linux el propio explorador de archivos suele dar la opción de hacerlo. 

Por ejemplo, en Ubuntu solo tenemos que abrir el explorador de archivos e ir a *Otras Ubicaciones/Other Locations* y escribir abajo del todo (donde pone *Connect yo Server*) la sentencia
```
sftp://USER@picasso.scbi.uma.es
```
Donde USER debe de sustituirse por el usuario correspondiente. 

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/sftp_Ubuntu.png" align=center width='800px'/>
<center>Entrar en Picasso mediante el explorador de archivos de Ubuntu.</center>
</center></figure>

En otros exploradores de archivos como pueden ser Dolphin (el que trae por defecto OpenSuse con el escritorio KDE), simplemente hay escribir la sentencia anterior en la linea de la ruta

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/sftp_suse.png" align=center width='800px'/>
<center>Entrar en Picasso mediante el explorador de archivos de Ubuntu.</center>
</center></figure>

<a id='sec_recursos_hardware'></a>
## 4. Recursos hardware

Picasso consta de diferentes tipos de nodos: unos con más Ram, otro con más cores, unos con procesador Intel, otros con AMD,...

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/Hardware_Picasso_Nodos_2024.png" align=center width='800px'/>
<center>Resursos Hardware de Picasso</center>
</center></figure>

Desde el punto de vista del usuario, no hay que preocuparse ni pensar el el tipo de nodos de Picasso. Como veremos en la sección [7. Sistema de colas](#sec_Sistema_de_colas), el usuario solo tiene que pedirle al sistema la RAM, el número de cores, el tiempo de ejecución y poco más, y es el sistema el que se carga de asignarle los recursos. Aquí lo único que tenemos que tener es que hay los nodos de más RAM o más cores son escasos en comparación con el resto, así que si se piden **más de 439GB de RAM** o **más de 128 cores por nodo**, los trabajos tardarán más en entrar a ejecución. 

También vemos que solo 4 nodos tiene GPU. Veremos en la sección [10. Usando GPUs](#sec_usando_GPUs) como usar estos nodos.

<div class=\"alert alert-block alert-danger\">
<b>Nota</b>: <i>RAM disponible</i>
Los valores de memoria RAM de la tabla anterior son "brutos". Para el usuario los valores disponibles son:
- sd nodes: 182 GB  (128 nodos)
- sr nodes: 439 GB  (156 nodos)
- bc nodes: 683 GB  (34 nodos)
- bl nodes: 1855 GB (24 nodos)
Aquí vemos bien lo comentado de que si pedimos más de 439 GB de RAM, los nodos disponibles se reducen drasticamente
</div>

<a id='sec_sistema_ficheros'></a>
## 5. Sistema de ficheros / cuota

Picasso consta de dos **sistemas de ficheros compartidos** (el HOME y el FSCRATCH), a parte de un **sistema de ficheros local** de cada nodo (LOCALSCRATCH). Cada usuario tiene un **cuota** de ficheros y espacio en HOME y otra en FSCRATCH.

### 5.1. Sistemas de ficheros compartidos

En estos es en los que se trabaja la inmensa mayor parte del tiempo:

- HOME (Sistema de almacenamiento permanente): Aquí se deben almacenar los datos importantes, scripts de desarrollo propio, resultados finales y otros ficheros importantes. Para volver a tu home, puedes ingresar alguno de los siguientes comandos:
```
cd
cd ~ 
cd $HOME
```

- FSCRATCH (Sistema de almacenamiento temporal): FSCRATCH es un almacenamiento de alta velocidad en el que se deberían lanzar tus trabajos. Este sistema es temporal, es decir, **tiene una política de borrado automático de archivos antiguos (más de 2 meses)**. Es importante pues acordarse de copiar los resultado importantes al HOME una vez terminada la ejecución del trabajo. Para acceder a el se puede usar el comando:
```
cd $FSCRATCH
```
Se pueden copiar carpetas de HOME a FSCRATCH usando un comando como:
```
cp -r $HOME/path/to/your/folder/in/home $FSCRATCH/path/to/target/folder
```
o desde $FSCRATCH a $HOME usando
```
cp -r $FSCRATCH/path/to/your/folder/in/fscratch $HOME/path/to/target/folder
```

### 5.2. Quota

Cada usuario tiene un **cuota** de ficheros y espacio en HOME y otra en FSCRATCH. La cuota puede consultarse usando el comando 
```
quota
```
Cuando se haya sobrepasado alguna de las cuotas, aparecerá un mensaje a la entrada de Picasso avisando. Este mensaje puede nuevamente volver a ver usando el comando `quota`
<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/quota.jpg" align=center width='800px'/>
<center>Ejemplo de mensaja de cuota superada</center>
</center></figure>

Como podemos ver en a imagen, hay un cuota de **espacio** (en GB o TB) y otra de **número de ficheros**. Vemos además que hay dos tipos de cuotas:
- **Quota (quota soft)**: Una vez superada alguna de las cuotas soft, se otroga un periodo de gracia de 7 días para volver a la situación normal. Transcurridos estos 7 días con la cuota superada, **se bloquea la escritura**.
- **Limit (quota hard)**: La cuota hard no se puede superar. Cuando se alcanza **se bloquea la escritura**.

<a id='sec_software'></a>
## 6. Software

En Picasso hay preinstalada una gran variadad de softwares. Pueden consultarse esta lista o bien [en la web del centro](https://www.scbi.uma.es/site/scbi/software) o mediante el comando
``` 
module avail | grep -i software_name
```
Para cargar un software se usa el comando
```
module load software/version
```
Para ver los modulos cargados, se usa el comando:
```
module list
```
Para descargar un modulo
```
module unload software/version
```
Para descargar todos los modulos
```
module purge
```

<a id='sec_Sistema_de_colas'></a>
## 7. Sistema de colas

### 7.1. Archivo de envio (simple)

Para acceder a todos los recursos de Picasso hay que usar el **sistema de colas**. Cuando se accede a Picasso, se accede a uno de los nodos del superordenador. Al resto de nodos no se puede acceder directamente, sino que lo que se hace es enviar los trabajos al sistema de colas. Para ello, se debe de escribir un "archivo de envio" donde se especifican los recursos necesarios, se cargan los módulos necesario y se ejecuta el programa. 

Veamos un ejemplo simple de archivo de envio:
```
#!/usr/bin/env bash
#SBATCH -J esto_es_un_ejemplo
#SBATCH --cpus-per-task=2
#SBATCH --mem=2gb
#SBATCH --time=10:00:00
#SBATCH --constraint=cal

# Set output and error files
#SBATCH --error=ejemplo_simple.%J.err
#SBATCH --output=ejemplo_simple.%J.out

module load software/version

hostname

time ./mi_programa -t $SLURM_CPUS_PER_TASK argumentos  
```

Donde el `%J` en el nombre de los archivos de salida se sustituye por el id del trabajo, de forma que los ficheros de salida no se pisan unos a otros.

### 7.2. Envío al sistema de colas

Una vez escrito este fichero, hay que **enviarlo al sistema de colas**. Para ello se usa el comando
```
sbatch script_de_envio.sh
```

Puede verse la cola con el comando
```
squeue
```

Puede cancelarse en envio de un trabajo con el comando
```
scancel job_id
```
donde `job_id` se sustituye por el id del trabajo 

<a id='sec_array_jobs'></a>
## 8. Array jobs

<a id='sec_seleccion_de_recursos'></a>
## 9. Selección de recursos

<a id='sec_usando_GPUs'></a>
## 10. Usando GPUs