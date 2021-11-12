#!/bin/bash
#A script to climb backwards

END=$1
for i in $(seq 1 $END); do
	cd ../
done
