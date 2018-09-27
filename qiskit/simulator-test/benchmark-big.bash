#!/bin/bash

# ---------
# file name 
# ---------

today=`date '+%Y_%m_%d_%H_%M_%S'`;
outfname="big_timing_$today.txt"

# -----------------------
# benchmark the simulator
# -----------------------

for n in 25
do
    for d in 5 10 15 20 25 30
    do
        python simulator-test.py $n $d >> $outfname
    done
done
