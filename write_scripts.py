# Start by importing necessary modules
import accelerometer
from accelerometer import accUtils


# The structure of the 0 folder is different 
# The structure of the other folders is all the same 

# There are 4 different outputs we wish to process 
## - 5 sec epochs: basic vars : five_sec_basic
## - 30 sec epochs: Walmsley classification : walmsley
## - 30 sec epochs: Willetts classification, full feature set : willetts_full
## - 30 sec epochs: Willetts classification, reduced feature set : willetts_reduced

# Let's make a loop which: 
#   - Identifies correct folder structure 
#   - Writes commands for each of the above options


for i in range(5):
    for j in range(11):
        
        
        # Describe the output folder
        out_folder_string = "repeat" + str(i)
        
        
        # Describe the input folder - note folder structure differs for 0 vs 1 to 4
        if (i == 0):
            if (j == 0):  
                in_folder_string = out_folder_string
                in_folder_string_long = out_folder_string
            else: 
                in_folder_string = "do_not_run" # This is inelegant but basically we want to only generate the set of commands once for repeat 0

        
        else: 
            in_folder_string = "repeat" + str(i) + "-subfolder-" + str(j)
            in_folder_string_long = "repeat" + str(i) + "/" + in_folder_string + ".0"
        
        
        print(in_folder_string) # visual check
        
        
        # Now do the command generation
        if not in_folder_string == "do_not_run": 

            # five_sec_basic 
            accUtils.writeStudyAccProcessCmds("/well/doherty/projects/ukb-season-repeats-59070/" + in_folder_string_long + "/rawData/", 
            outDir = "/well/doherty/projects/ukb-season-repeats-59070/processed_oct21/" + out_folder_string + "/oct21_five_sec_basic/", 
            accExt = ".cwa.gz", 
            cmdsFile = "processCmds/five_sec_basic/oct21_five_sec_basic_commands_"+ in_folder_string +  ".txt", 
            cmdOptions = "--epochPeriod 5 --activityClassification False --intensityDistribution True --deleteIntermediateFiles False"
        )

            # walmsley
            accUtils.writeStudyAccProcessCmds("/well/doherty/projects/ukb-season-repeats-59070/" + in_folder_string_long + "/rawData/", 
                outDir = "/well/doherty/projects/ukb-season-repeats-59070/processed_oct21/" + out_folder_string + "/oct21_walmsley/", 
                accExt = ".cwa.gz", 
                cmdsFile = "processCmds/walmsley/oct21_walmsley_commands_" + in_folder_string + ".txt", 
                cmdOptions = "--activityModel walmsley --deleteIntermediateFiles False"
            )

            # willetts_full
            accUtils.writeStudyAccProcessCmds("/well/doherty/projects/ukb-season-repeats-59070/" + in_folder_string_long + "/rawData/", 
                outDir = "/well/doherty/projects/ukb-season-repeats-59070/processed_oct21/" + out_folder_string + "/oct21_willetts_full/", 
                accExt = ".cwa.gz", 
                cmdsFile = "processCmds/willetts_full/oct21_willetts_full_commands_" + in_folder_string + ".txt", 
                cmdOptions = "--activityModel willetts --deleteIntermediateFiles False --processInputFile False"
        )

            # willetts_reduced
            accUtils.writeStudyAccProcessCmds("/well/doherty/projects/ukb-season-repeats-59070/" + in_folder_string_long + "/rawData/", 
                outDir = "/well/doherty/projects/ukb-season-repeats-59070/processed_oct21/" + out_folder_string + "/oct21_willetts_reduced/", 
                accExt = ".cwa.gz", 
                cmdsFile = "processCmds/willetts_reduced/oct21_willetts_reduced_commands_" + in_folder_string + ".txt", 
                cmdOptions = "--activityModel /well/doherty/users/llz512/home/repeatedMeasurementsProcessing/models/willetts-jan21-reduced-feature-set.tar --deleteIntermediateFiles False --processInputFile False"
        )


