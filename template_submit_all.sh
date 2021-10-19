qsub  oct21_five_sec_basic_commands_repeat0.sh
for i in {1..4}
do
    for j in {0..10}
    do
        qsub oct21_five_sec_basic_commands_repeat$i-subfolder-$j.sh
    done
done
