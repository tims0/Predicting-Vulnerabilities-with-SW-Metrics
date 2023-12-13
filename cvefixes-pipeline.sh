#!/bin/bash
COMMAND="error"
INPUT="all"
MODEL="all"
SUBSET="both"
TYPE="all"

if [ "$1" = "--updateDatabase" ]; then
    COMMAND="updateDatabase"
elif [ "$1" = "--extractMetrics" ]; then
    COMMAND="extractMetrics"
    INPUT=$2
elif [ "$1" = "--preprocessDataset" ]; then
    COMMAND="preprocessDataset"
    INPUT=$2
elif [ "$1" = "--correlationAnalysis" ]; then
    COMMAND="correlationAnalysis"
    INPUT=$2
elif [ "$1" = "--featureSelection" ]; then
    COMMAND="featureSelection"
    INPUT=$2
elif [ "$1" = "--performModelExecution" ]; then
    COMMAND="performModelExecution"
    INPUT=$2
    if [ "$3" = "--model" ]; then
        MODEL=$4
    elif [ "$3" = "--subset" ]; then
        SUBSET=$4
    elif [ "$3" = "--type" ]; then
        TYPE=$4
    fi
    if [ "$5" = "--model" ]; then
        MODEL=$6
    elif [ "$5" = "--subset" ]; then
        SUBSET=$6
    elif [ "$5" = "--type" ]; then
        TYPE=$6
    fi
    if [ "$7" = "--model" ]; then
        MODEL=$8
    elif [ "$7" = "--subset" ]; then
        SUBSET=$8
    elif [ "$7" = "--type" ]; then
        TYPE=$8
    fi
fi

python3 main.py $COMMAND $INPUT $SUBSET $TYPE $MODEL