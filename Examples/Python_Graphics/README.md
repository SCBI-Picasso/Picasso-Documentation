In this folder you can find an example of how to generate a graph with python by sending the job to the queuing system. 

As you can see, there are two scripts:
- python_script.py: python script that generates the graph and saves it.
- send_python.sh: Script to send to the queue system the python script.

To send this job to the queueing system, just copy these scripts and run
```
sbatch send_python.sh
```

You can view you queue using the command
```
squeue
```

When the job is finished, you can check the .err file for errors and the .out file for program outputs (such as prints).