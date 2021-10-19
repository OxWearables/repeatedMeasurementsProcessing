# Import subprocess to run bash from python
import subprocess 
import sys

# Loop through
for runtag in ['five_sec_basic', 'walmsley', 'willetts_full', 'willetts_reduced']: 
    for i in range(5): 
        for j in range(11):
            # subprocess.run("ls /well/doherty/users/llz512/home/repeatedMeasurementsProcessing")
            if i == 0:
                if j == 0:
                    result = subprocess.run(["/well/doherty/users/llz512/home/repeatedMeasurementsProcessing/python-env-skylake/bin/python", "/well/doherty/users/llz512/home/repeatedMeasurementsProcessing/clusterProcessing/write-BMRC-script.py", "oct21_"+ runtag + "_commands_repeat0.txt",  "--logDir",  "/well/doherty/projects/ukb-season-repeats-59070/processed_oct21/repeat0/oct21_" + runtag + "/clusterLogs/",  "--projectVirtualEnvPath",  "/well/doherty/users/llz512/home/repeatedMeasurementsProcessing/python-env-"], cwd = "/well/doherty/users/llz512/home/repeatedMeasurementsProcessing/processCmds/" + runtag + "/")
                    
            if not i == 0: 
                subprocess.run(["/well/doherty/users/llz512/home/repeatedMeasurementsProcessing/python-env-skylake/bin/python", "/well/doherty/users/llz512/home/repeatedMeasurementsProcessing/clusterProcessing/write-BMRC-script.py", "oct21_"+ runtag + "_commands_repeat" + str(i) + "-subfolder-" + str(j) + ".txt", "--logDir", "/well/doherty/projects/ukb-season-repeats-59070/processed_oct21/repeat" + str(i) + "/oct21_" + runtag + "/clusterLogs/", "--projectVirtualEnvPath",  "/well/doherty/users/llz512/home/repeatedMeasurementsProcessing/python-env-"], cwd = "/well/doherty/users/llz512/home/repeatedMeasurementsProcessing/processCmds/" + runtag + "/")
        

