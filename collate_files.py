import accelerometer
from accelerometer import accUtils

for runtag in ['five_sec_basic', 'walmsley', 'willetts_full', 'willetts_reduced']:
    for i in range(5):
        accUtils.collateJSONfilesToSingleCSV("/well/doherty/projects/ukb-season-repeats-59070/processed_oct21/repeat" + str(i) + "/oct21_" + runtag + "/summary/", "/well/doherty/projects/ukb-season-repeats-59070/processed_oct21/summary_files/oct21_repeat" + str(i) + "_" + runtag + "_summary.csv")




