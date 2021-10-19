# Generate scripts
python write_scripts.py

# Retrofit how to call correct epoch folder
sed -i 's/oct21_willetts_full\/epoch/oct21_walmsley\/epoch/g' processCmds/willetts_full/*
sed -i 's/oct21_willetts_reduced\/epoch/oct21_walmsley\/epoch/g' processCmds/willetts_reduced/*

# Retrofit new syntax for calling accProcess from accelerometer
sed -i 's/python3 accProcess.py/accProcess/g' processCmds/*/*
