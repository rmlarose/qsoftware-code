#!/bin/bash

# ---------
# variables
# ---------

export OMP_NUM_THREADS=2
export OMP_PROC_BIND=spread

# ---------
# file name 
# ---------

today=`date '+%Y_%m_%d_%H_%M_%S'`;
outfname="timing_$today.txt"

# -----------------------
# benchmark the simulator
# -----------------------

for n in 16 17 18 19 20 21 22 23 24 25 26 27 28
do
    for d in 5 10 15 20 25 30
    do
        python simulator-test.py $n $d >> $outfname
    done
done
