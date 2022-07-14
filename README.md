# repeatedMeasurementsProcessing

- Generate command files with `generate_command_files.sh`
- Generate bash scripts with `write_cluster_scripts.py`
- Write a `submit_all.sh` script for each command script directory, as per `template_submit_all.sh` 
- `cd` to each command script directory and run `qsub submit_all.sh` 
- Note that runs `willetts_full` and `willetts_reduced` only run after run `walmsley` has finished, as all three use the same `epoch` files. 
- Use `collate_files.py` to collate files into single csv files. 
