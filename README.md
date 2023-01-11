# repeatedMeasurementsProcessing

This folder contains scripts for processing raw accelerometer data from participants with repeated measurements. 

## Notes
Please note that:

- This code is in active development.
- It is shared as-is to enable scientific reproducibility and 'open science'.
- This code is not shared for the purpose of general use; any use is strictly at your own risk.
- In particular, it is not an authoritative source, and has not been reviewed or tested.

Please share comments, suggestions and errors/bugs found, either directly on the GitHub page or by emailing rosemary.walmsley@gtc.ox.ac.uk.

## How code in this folder was used: 

- Generate command files with `generate_command_files.sh`
- Generate bash scripts with `write_cluster_scripts.py`
- Write a `submit_all.sh` script for each command script directory, as per `template_submit_all.sh` 
- `cd` to each command script directory and run `qsub submit_all.sh` 
- Note that runs `willetts_full` and `willetts_reduced` only run after run `walmsley` has finished, as all three use the same `epoch` files. 
- Use `collate_files.py` to collate files into single csv files. 
