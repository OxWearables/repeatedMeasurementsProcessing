# Generate scripts
python write_scripts.py

# Retrofit how to call correct epoch folder
for i in {0..4}
do
    sed -i 's/oct21_willetts_full\/epoch/oct21_walmsley\/epoch/g' processCmds/willetts_full/*
    sed -i 's/oct21_willetts_reduced\/epoch/oct21_walmsley\/epoch/g' processCmds/willetts_reduced/*
done

# Retrofit new syntax for calling accProcess from accelerometer
sed -i 's/accProcess.py/accProcess/g' processCmds/*/*
