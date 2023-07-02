# Picasso Documentation

This is the official documentation for Picasso supercomputer usage. If you have any problem that is not specified on 
this documentation or in the [frequently asked questions](#sec_7) section please, contact us at 
```
soporte@scbi.uma.es.
```
# Index

- [1 - Citation and akcnowledges](#sec_1)
- [2 - About Picasso: Harware and Filesystems](#sec_2)
    - [2.1 - System overview](#sec_2.1)
    - [2.2 - Hardware resources](#sec_2.2)
        - [2.2.1 - Total compute resources](#sec_2.2.1)
        - [2.2.2 - Available resources](#sec_2.2.2)
    - [2.3 - File system](#sec_2.3)
        - [2.3.1 - Picasso Filesystems](#sec_2.3.1)
        - [2.3.2 - File and space quota](#sec_2.3.2)
        - [2.3.3 - Fast scratch filesystem (FSCRATCH)](#sec_2.3.3)
        - [2.3.4 - Local scratch filesystem](#sec_2.3.4)
        - [2.3.5 - Backup policy](#sec_2.3.5)
- [3 - Login to Picasso](#sec_3)
    - [3.1 - SSH connection](#sec_3.1)
    - [3.2 - Terminal](#sec_3.2)
    - [3.3 - Important notice](#sec_3.3)
- [4 - Copy files from/to picasso](#sec_4)
    - [4.1 - Downloading files from internet](#sec_4.1)
    - [4.2 - Copying files from your computer to picasso and viceversa ](#sec_4.2)
- [5 - Software](#sec_5)
    - [5.1 - Installed software](#sec_5.1)
    - [5.2 - Loaded software](#sec_5.2)
    - [5.3 - Compiling software](#sec_5.3)
- [6 - How to send jobs](#sec_6)
    - [6.1 - Preparing to send a job](#sec_6.1)
    - [6.2 - Modifying resources and limits](#sec_6.2)
    - [6.3 - Asking for GPUs](#sec_6.3)
    - [6.4 - Sample jobs generator](#sec_6.4)
    - [6.5 - Sending a job](#sec_6.5)
    - [6.6 - Array jobs: how to send lots of jobs](#sec_6.6)
    - [6.7 - Monitoring queued jobs](#sec_6.7)
    - [6.8 - Cancelling jobs](#sec_6.8)
    - [6.9 - Using the LOCALSCRATCH filesystem](#sec_6.9)
- [7 - FAQs](#sec_7)


[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)



# 1 - Citation and akcnowledges <a id="sec_1"></a>

If you use our resources, you must acknowledge this service on your publications. Please, add a text like this:

    The authors thank the Supercomputing and Bioinnovation Center (SCBI) of the University of Malaga for their provision 
    of computational resources (the supercomputer PIcasso) and technical support (www.scbi.uma.es/site)

We would appreciate if you could inform us of your publications that used our resources, and we will take the opportunity
to congratulate you.

[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)




# 2 - About Picasso: Harware and Filesystems <a id="sec_2"></a>

## 2.1 - System overview <a id="sec_2.1"></a>

SCBI's supercomputing resources comprises a set of computation nodes with different characteristics. 
However, all those machines are unified behind a single **Slurm** queue system instance, so you shouldn't worry about their 
differences, as you only have to create a SBATCH script (a text file with some special syntax).

The script is used to **request the resources** (time, cpus, memory, gpus, etc) that your job will use. It is important 
that the resources asked can be optimally used, as this will help your job to start as soon as possible. Machines with 
special characteristics like a more memory or gpus are scarse, and because of that they are harder to reserve. 

Once you have your script written, you have to send it to the **queue system**. Then the queue system will analyze your 
request and send the job to the appropriate computers. There are some examples in chapter 
[How to send jobs](#sec_6). If you have any question, please, don't hesitate in contacting us at 
soporte@scbi.uma.es and we will do our best to try to help you.


## 2.2 - Hardware resources <a id="sec_2.2"></a>

### 2.2.1 - Total compute resources <a id="sec_2.2.1"></a>

In Picasso we have the following nodes:

- **sd nodes**: 126 x SD530 nodes: 52 cores (Intel Xeon Gold 6230R @ 2.10GHz), 192 GB of RAM. 
InfiniBand HDR100 network. 950 GB of localscratch disks

- **bl nodes**: 24 x Bull R282-Z90 nodes: 128 cores (AMD EPYC 7H12 @ 2.6GHz), 2 TB of RAM. 
InfiniBand HDR200 network. 3.5 TB of localscratch disks.

- **sr nodes**: 156 x Lenovo SR645 nodes: 128 cores (AMD EPYC 7H12 @ 2.6GHz), 512 GB of RAM. 
InfiniBand HDR100 network. 900 GB of localscratch disks.

- **exa (GPU) nodes**: 4 x DGX-A100 nodes: 8 GPUs (Nvidia A100), 1 TB of RAM. 
InfiniBand HDR200 network. 14 TB of localscratch

### 2.2.2 - Available resources <a id="sec_2.2.2"></a>

Both the operating system and the file system require part of the resources (RAM) available on the nodes. For this 
reason, the resources (CPUs, RAM) that can be requested for each node through the queuing system are as follows:

- **sd nodes**: CPUs: 52 cores. RAM: 182 GB

- **bl nodes**: CPUs: 128 cores. RAM: 1855 GB

- **sr nodes**: CPUs: 128 cores. RAM: 439 GB

- **exa (GPU) nodes**: CPUs: 128 cores. RAM: 878 GB

<span style="color: red"> IMPORTANT </span>: The resources of the Exa nodes are distributed among the 8 GPUs of each 
node, so in ideal usage no more than 16 cores and 109 GB of RAM should be requested per GPU requested.

<span style="color: red"> IMPORTANT </span>: if you aim to use a lot of files (ie. more than 15000) to solve a problem 
(for example, in IA training), you must contact with us first, because it can lead to serious performance problems.


## 2.3 - File system <a id="sec_2.3"></a>

### 2.3.1 - Picasso Filesystems  <a id="sec_2.3.1"></a>

The Picasso filesystem is divided in two physically independent spaces. In both of them, as a user of picasso, you will 
get some disk quota. The quota determines the disk limits for your user.

- **HOME** (*Permanent storage system*): Here you should store input data, your own developed scripts, final results, 
and other important data. To go to your home space you can enter one of the following commands:

```
    cd
```
```
    cd ~
```
```
    cd $HOME
```

- **FSCRATCH** (*Temporal storage system*): FSCRATCH is a very high speed storage in which you should launch your work.
You can find relevant information about using FSCRATCH in section [Fast scratch filesystem (FSCRATCH)](#sec_2.3.3). 
Be aware that FSCRATCH is a temporary storage, and old files will be deleted periodically. 
<span style="color: red">  PLEASE, DO NOT USE IT TO STORE IMPORTANT DATA </span>. 
To go to your fscratch space you can enter:

```
    cd $FSCRATCH
```



### 2.3.2 - File and space quota <a id="sec_2.3.2"></a>

Apart from the **space limitation** in each of both spaces (home and fscratch), there is also a **file quota**. While 
the space quota determines the limitation in terms of gigabytes written, the file quota determines the limitation in 
terms of number of files written.

The quota works in two steps, that are called soft quota and hard quota: 

- **Soft quota**:  When you exceed your quota, you will receive a warning message every time you log into picasso, 
In the figure below, you can see an example of someone exceeding the soft quota of free space.

<div style="text-align:center">
<img src="Figuras/Cuota_7_dias.png" width="1000"/>
</div>

- **Hard quota**: When you exceed your quota by a lot, you will find a hard limit which will not allow you to write any
more files, even if you were inside the 7 days of soft quota grace period.

One the cuota is reached (space or file quota), you have 7 days to return to the normal situation. If those 7 days pass
or the hard quota is reached, the disk writing will be blocked. 

In order to check your quotas, you can run the command:
```
mmlsquota
```


### 2.3.3 - Fast scratch filesystem (FSCRATCH) and purging policy <a id="sec_2.3.3"></a>

**- About FSCRATCH**

The FSCRATCH (Fast Scratch) filesystem should be used to speed up the jobs, specially the ones that make an intense use 
of the storage. This space is conceived as a pseudo-volatile filesystem. This means that the data stored here will be 
deleted periodically and automatically, so <span style="color: red"> you should not use it for storaging important files.
</span>:


To go to FSCRATCH, type 
```
cd $FSCRATCH
```
You can copy folders from HOME to FSCRATCH using command like:
```
cp -r $HOME/path/to/your/folder/in/home $FSCRATCH/path/to/target/folder
```
or from FSCRATCH to HOME using
```
cp -r $FSCRATCH/path/to/your/folder/in/fscratch $HOME/path/to/targe/folder
```

Don't forget to copy the important output data back to your HOME, because it 
will be deleted after some weeks.

**- Purging policy**

The files that have not been used for more than two months will be deleted automatically. 

Files will not be deleted after exactly two months, but files that have not been used for two months will be subject to 
deletion at any time without prior notice. The purge is triggered depending on the percentage of **total** FSCRATCH usage.

If you are not sure how to use FScratch, please contact us to soporte@scbi.uma.es.

### 2.3.4 - Local scratch filesystem <a id="sec_2.3.4"></a>

There are some nodes that have a local scratch filesystem. This local scratch is even faster than the fscratch 
filesystem, but it has a main disadvantage: It is only accessible from each node, so you cannot access it from the login
machine, but only from inside the SBATCH script that you will send to the queue system (using the $LOCALSCRATCH 
environment variable).

The local scratch is very fast, and may speed up some jobs substantially when used. And it's a must when a job needs to 
write lots of files or to make an intense disk usage.  You can also find an example in the section 
[How to send jobs](#sec_6).

If you think you need access to local scratch and you are not sure how to use it, please contact us to 
soporte@scbi.uma.es.

### 2.3.5 - Backup policy <a id="sec_2.3.5"></a>

<span style="color: red"> IMPORTANT NOTE </span>: It is important that you follow a responsible backup policy. We are 
not liable for the loss of data stored in our systems, so if your data is important, you should have backups of it in 
your own machine or backup system. As a courtesy we maintain a backup of the files stored in the home directory, but we 
cannot neither warranty it nor make backups of all the space available. You can follow these backup guidelines if you 
like:

- It is a good habit to use a version control system for your own programs and scripts. Git can be a good solution 
(https://git-scm.com/). Version control systems helps programmers to keep a tracking of all changes made to source code, 
scripts, etc... Every time that you make a change to a file, you can save it to your version control system with some 
textual description, and you can later see those changes at anytime or go back to an older version. 
This is not a true backup, but a kind of.

- Keep different backups, from different dates. Backup are also useful if you delete of modify a file by mistake.

- Store backups in different physical places. This way, if your main computer location suffers a disaster, you could 
access another copy that you have in another place.

- Try to access your backup data periodically. You can make lots of backups, but if they are not accessible they are 
not useful.

[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)

# 3 - Login to Picasso <a id="sec_3"></a>

Like most supercomputers, Picasso is based on a Linux distribution, in this case openSuse Leap 15.4. Remote system 
access is done by SSH protocol (port 22), connecting to a login server. In this server you will find all compilers and 
tools needed to prepare and send your jobs to the queue system.



## 3.1 - SSH connection <a id="sec_3.1"></a>

To connect to the login server you will need to enter the following command on the **system terminal** (it can be CMD or
PowerShell in Windows, or the terminal of Linux and MacOs):
```
ssh <username>@picasso.scbi.uma.es
```
For example, if your username is *myuser*, you should enter:
```
myuser@picasso.scbi.uma.es
```
After this, you will be prompted to enter your password. When entering it, you will see that **nothing appears on the** 
**screen**, but it is being registered. Press enter when you are done, and the connection should be established.

<span style="color: red">  Warning </span>: If you fail to enter the password for several times, the system will block 
your IP. It will be unblock after 30 minutes. If you fail serveral times again, the ip will be permanently blocked. You 
will have to contact us to soporte@scbi.uma.es in order to get unbanned.

Tip: if you have session issues and your connection brokes after a short innactivity time or because of Internet 
connection stability; you must include a keep alive command in your connections:
```
ssh ServerAliveInterval=60 myuser@picasso.scbi.uma.es
```

## 3.2 - MobaXTerm <a id="sec_3.2"></a>

If you are not familiar with terminals, maybe you can try to use program [MobaXTerm](https://mobaxterm.mobatek.net/). 
It is more user fiendly and allow thing like copy a file using the mouse. 

## 3.3 - Important notice <a id="sec_3.3"></a>

<span style="color: red">  IMPORTANT NOTE </span>: When you access Picasso, you are entering one of our nodes, the 
**login node**. The login node is not a place to execute your work. It can be used for building scripts, compiling 
programs, testing that a complex command that you are going to use in the SBATCH script is launching correctly, etc, 
but NOT for making real work.  All launched programs will be automatically killed without previous notice when they use 
more than 10 minutes of cpu time.

Real woks must be send to the **queue system** (see section [How to send jobs](#sec_6)).


[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)


# 4 - Copy files from/to picasso <a id="sec_4"></a>

At sometime you will need to copy files from, or into, picasso. We have to differentiate two cases: 

## 4.1 - Downloading files from internet <a id="sec_4.1"></a>

In case you want to **download** a file into picasso from a url available on **internet**, you can download it using wget 
command in picasso console:
```
wget <url>
```
For example, to download a file from the url https://www.example.com/file.txt, you have to use:
```
wget https://www.example.com/file.txt
```
It is usual that wget <url> command does not work when the file you need to download requires you to enter a password, 
to login into some account, or to make some other action before downloading. In these cases you will need to install a 
plugin for your web browser. This plugin will generate the complete working wget command for you. Then you will just 
have to paste the command in picasso and wait for the download to finish. These are the steps you need to follow:

1. Download and install one of these plugins depending on the web browser that you use 
([curlwget](https://chrome.google.com/webstore/detail/curlwget/dgcfkhmmpcmkikfmonjcalnjcmjcjjdn) for chrome, 
[cliget](https://addons.mozilla.org/es/firefox/addon/cliget/) for firefox, 
[curlwget](https://microsoftedge.microsoft.com/addons/detail/curlwget/njimejjehbbfhipbgakbleoobdgdcmof) for edge).

2. Start the download (in your computer) of the file you are interested in, then stop the download.

3. Now click on the plugin icon (usually in the top right corner of your web browser).

4. The complete wget command should appear. Copy the complete wget command.

5. Paste it in picasso and press enter. The download should start.




## 4.2 - Copying files from your computer to picasso and viceversa <a id="sec_4.2"></a>

### 4.2.1 - Scp command

In case you need to *copy* a file from/to picasso to/from your computer, you can use the comand 
```
scp -r <from_path_file> <to_destination_path>
```
This command can be used to copy in both directions.

**To copy from picasso to your computer:**
```
scp -r <user>@picasso.scbi.uma.es:<file_path_in_picasso> <file_local_destination>
```
You can obtain the path to a folder in Picasso using the comand 
```
pwd
```
You have to move to the folder you want to copy and execute this command.

**To copy from your computer to picasso:**
```
scp <file_local_destination> <user>@picasso.scbi.uma.es:<file_destination_in_picasso>
```
To get its local path on your computer, you can simply click on the top bar of the file explorer and copy the path, 
as you can see in the figure 
<div style="text-align:center">
<img src="Figuras/File_explorer.png" width="1000"/>
</div>

### 4.2.2 - Rsync command

If you want to copy a lot of files, we recommend the use of the rsync command, is very similar to scp, but rsync can 
skip already transferred files, so it makes a synchronization instead of a full copy. The sintax is very similar 

**To copy from picasso to your computer:**
```
rsync -CazvHu <user>@picasso.scbi.uma.es:<file_path_in_picasso> <file_local_destination>
```
**To copy from your computer to picasso:**
```
rsync -CazvHu <file_local_destination> <user>@picasso.scbi.uma.es:<file_destination_in_picasso>
```
<span style="color: red">  NOTE </span>: For heavy transfers we recommend using the rsync command, since if the transfer 
is interrupted by any reason it will skip existing files when you try to upload them again.



[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)

# 5 - Software <a id="sec_5"></a>

## 5.1 - Installed software <a id="sec_5.1"></a>

We have a wide variety of software installed ready to use. You can browse the updated list in our 
[web](https://www.scbi.uma.es/site/scbi/software), or by executing this command on the login server:
```
module avail
```
Para buscar un software específico
```
module avail | grep -i <software>
```
Por ejemplo, para buscar las instalaciones de un software como el WRF (Weather Research and Forecasting), se puede usar
el comando
```
module avail | grep -i wrf
```




## 5.2 - Loaded software <a id="sec_5.2"></a>

## 5.3 - Compiling software <a id="sec_5.3"></a>


[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)

# 6 - How to send jobs <a id="sec_6"></a>

## 6.1 - Preparing to send a job  <a id="sec_6.1"></a>

## 6.2 - Modifying resources and limits <a id="sec_6.2"></a>

## 6.3 - Asking for GPUs <a id="sec_6.3"></a>

## 6.4 - Sample jobs generator <a id="sec_6.4"></a>

## 6.5 - Sending a job <a id="sec_6.5"></a>

## 6.6 - Array jobs: how to send lots of jobs <a id="sec_6.6"></a>

## 6.7 - Monitoring queued jobs <a id="sec_6.7"></a>

## 6.8 - Cancelling jobs <a id="sec_6.7"></a>

## 6.9 - Using the LOCALSCRATCH filesystem <a id="sec_6.7"></a>


[//]: <> (==============================================================================================================)
[//]: <> (=============================================== SECCION ======================================================)
[//]: <> (==============================================================================================================)

# 7 - FAQs <a id="sec_7"></a>

