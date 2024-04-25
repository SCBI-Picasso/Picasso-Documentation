# Curso rápido de introducción a Picasso

Autores:
- *Rafael Larrosa Jiménez (Administrador de Sistemas - SCBI)* 
- *David Castaño Bandín (Administrador de Sistemas - SCBI)*
- *Manuel Guerrero Claro (Administrador de Sistemas - SCBI)*


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
<img src="./Figuras/mapa_ICTS.jpg" align=center width='1000px'/>
<center>Mapa de las ICTS en España.</center>
</center></figure>

Un ejemplo muy conocido de este tipo de infraestructuras son los famosos telescopios y observatorios astronómicos situados en Canarias. Si nos centramos más en el ámbito andaluz, tenemos la *Reserva Biológica de Doñana*, el *Observatorio Astronómico de Calor Alto* o la que nos compete en este curso: la **Red Española de Supercomputación (RES)** a traves del nodo **Picasso**.

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/mapa_RES.png" align=center width='1000px'/>
<center>Mapa de las Red Española de Supercomputación (RES).</center>
</center></figure>

La RES está conformada por una serie de "nodos", es decir, una serie de **centros de supercomputación** repartidos por toda España. El SCBI con su supercomputador Picasso, con sus 40.000 núcleos, se situa como el **segundo nodo más potente de RES**, solo superado por el ampliamente conocido Marenostrum, situado en el BSC (Barcelona Supercomputer Center).

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/RES_grafica.png" align=center width='1000px'/>
<center>Gráfica de la potencia de los diferentes nodos de la RES.</center>
</center></figure>

El SCBI también está inmerso en Computación Cuántica a través del proyecto QuantumSpain.

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/Quantum.png" align=center width='1000px'/>
</center></figure>




<a id='sec_acceso'></a>
## 2. Acceso

El acceso a Picasso de sa usando el protocolo ssh en linea de comando:
```
ssh -X USER@picasso.scbi.uma.es
```
Donde USER debe de sustituirse por el usuario correspondiente. Este comando se puede ejecutar en:
- Un terminal de Linux
- Un terminal de MacOs
- Un PowerShell en Windows



<div class=\"alert alert-block alert-danger\">
<b>Nota</b>    

Al escribir la contraseña no aparecerá nada en pantalla. Puede desconcertar al principio pero no preocuparse, se está escribiendo igual.
</div>


Otra opción sería usar un software dedicado a las conexiones ssh con servidores, como puede ser [MobaXterm](https://mobaxterm.mobatek.net/) o similares. MobaXterm es una buena opción para principiantes que no estén acostumbrados a manejar un terminal, pues este presenta un explorador de ficheros (columana de la izquierda), lo que facilita el moverse entre carpetas y mover archivos entre Picasso y el ordenador local 

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/mobaXterm-ssh.png" align=center width='1000px'/>
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

### 3.1. El comando scp

### 3.2. El comando rsync

### 3.3. Mover ficheros con MobaXTerm

### 3.4. Otras alternativas 

Hay una gran variedad de softwares que permiten montar un servidor por sftp. Por ejemplo, las distribuciones de Linux el propio explorador de archivos suele dar la opción de hacerlo. 

Por ejemplo, en Ubuntu solo tenemos que abrir el explorador de archivos e ir a *Otras Ubicaciones/Other Locations* y escribir abajo del todo (donde pone *Connect ro Server) la sentencia
```
sftp://USER@picasso.scbi.uma.es
```
Donde USER debe de sustituirse por el usuario correspondiente. 

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/mobaXterm-ssh.png" align=center width='1000px'/>
<center>Entrar en Picasso mediante el explorador de archivos de Ubuntu.</center>
</center></figure>

En otros exploradores de archivos como pueden ser Dolphin (el que trae por defecto OpenSuse con el escritorio KDE), simplemente hay escribir la sentencia anterior en la linea de la ruta

<figure><center>
<a id='fig_ref'></a>
<img src="./Figuras/sftp_suse.png" align=center width='1000px'/>
<center>Entrar en Picasso mediante el explorador de archivos de Ubuntu.</center>
</center></figure>




<a id='sec_recursos_hardware'></a>
## 4. Recursos hardware

<a id='sec_sistema_ficheros'></a>
## 5. Sistema de ficheros / cuota

<a id='sec_software'></a>
## 6. Software

<a id='sec_Sistema_de_colas'></a>
## 7. Sistema de colas

<a id='sec_array_jobs'></a>
## 8. Array jobs

<a id='sec_seleccion_de_recursos'></a>
## 9. Selección de recursos

<a id='sec_usando_GPUs'></a>
## 10. Usando GPUs