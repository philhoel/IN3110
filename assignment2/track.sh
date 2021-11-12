#!/bin/bash

if [ "$1" == "start" ];
then
    x=`tail -1 logfile.txt`
    if [ "$x" == "started" ];
    then
        echo Tracker already running
    else
        echo `date`
        echo `date` >> logfile.txt
        echo $@ >> logfile.txt
        echo started >> logfile.txt
    fi
elif [ "$1" == "stop" ];
then
    x=`tail -1 logfile.txt`
    if [ "$x" == "stopped" ];
    then
        echo No task to stop
    else
        echo `date`
        echo `date` >> logfile.txt
        echo stopped >> logfile.txt
        
    fi
elif [ "$1" == "status" ];
then
    x=`tail -1 logfile.txt`
    if [ "$x" == "started" ];
    then
        tail -2 logfile.txt
    else
        echo No task is running
    fi
elif [ "$1" == "help" ];
then
    echo "How to use: use argument 'start' to start with optional task label, 'stop' to stop, 'status' to see what task are being tracked. Everthing is logged in logfile.txt"
else
    echo "Use argument 'help' for information about how to use"
fi