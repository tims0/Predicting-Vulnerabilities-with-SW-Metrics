import logging
import os
import subprocess
import sys
from config import config
import dataset_exploration
from tools import analizo, combined, understand

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "main.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def updateDatabase():
    subprocess.call(['sh', config.bash_cvefixes_from_scratch])
    dataset_exploration.performDatasetExploration()

def extractMetrics(input=config.arg_all):
    if input == config.arg_understand:
        understand.extractFileMetricsFromRepoUnderstand()
    elif input == config.arg_analizo:
        analizo.extractFileMetricsFromRepoAnalizo()
    elif input == config.arg_all:
        understand.extractFileMetricsFromRepoUnderstand()
        analizo.extractFileMetricsFromRepoAnalizo()
    else:
        logging.error("Error - Please use understand, analizo or all as argument")

def preprocessDataset(input=config.arg_all):
    if input == config.arg_understand:
        understand.preprocessFileDatasetUnderstand()
    elif input == config.arg_analizo:
        analizo.preprocessFileDatasetAnalizo()
    elif input == config.arg_combined:
        combined.preprocessFileDatasetCombined()
    elif input == config.arg_all:
        understand.preprocessFileDatasetUnderstand()
        analizo.preprocessFileDatasetAnalizo()
        combined.preprocessFileDatasetCombined()
    else:
        logging.error("Error - Please use understand, analizo, combined or all as argument")

def correlationAnalysis(input=config.arg_all):
    if input == config.arg_understand:
        understand.correlationAnalysisUnderstand()
    elif input == config.arg_analizo:
        analizo.correlationAnalysisAnalizo()
    elif input == config.arg_combined:
        combined.correlationAnalysisCombined()
    elif input == config.arg_all:
        understand.correlationAnalysisUnderstand()
        analizo.correlationAnalysisAnalizo()
        combined.correlationAnalysisCombined()
    else:
        logging.error("Error - Please use understand, analizo, combined or all as argument")

def featureSelection(input=config.arg_all):
    if input == config.arg_understand:
        understand.featureSelectionUnderstand()
    elif input == config.arg_analizo:
        analizo.featureSelectionAnalizo()
    elif input == config.arg_combined:
        combined.featureSelectionCombined()
    elif input == config.arg_all:
        understand.featureSelectionUnderstand()
        analizo.featureSelectionAnalizo()
        combined.featureSelectionCombined()
    else:
        logging.error("Error - Please use understand, analizo, combined or all as argument")

def performModelExecution(input=config.arg_all, subset=config.arg_subset_both, type=config.arg_all, model=config.arg_all):
    if input == config.arg_understand:
        understand.performUnderstand(subset, type, model)
    elif input == config.arg_analizo:
        understand.performAnalizo(subset, type, model)
    elif input == config.arg_combined:
        understand.performCombined(subset, type, model)
    elif input == config.arg_all:
        understand.performUnderstand(subset, type, model)
        understand.performAnalizo(subset, type, model)
        understand.performCombined(subset, type, model)
    else:
        logging.error("Error - Please use understand, analizo, combined or all as argument")

if __name__ == '__main__':
    arg_command = sys.argv[1]
    arg_input = sys.argv[2]
    arg_model = sys.argv[3]
    arg_subset = sys.argv[4]
    arg_type = sys.argv[5]
    if arg_input == "":
        arg_input = config.arg_all
    if arg_model == "":
        arg_model = config.arg_all
    if arg_subset == "":
        arg_subset = config.arg_subset_both
    if arg_type == "":
        arg_type = config.arg_all

    if arg_command == config.arg_command_updateDatabase:
        updateDatabase()
    elif arg_command == config.arg_command_extractMetrics:
        extractMetrics(arg_input)
    elif arg_command == config.arg_command_preprocessDataset:
        preprocessDataset(arg_input)
    elif arg_command == config.arg_command_correlationAnalysis:
        correlationAnalysis(arg_input)
    elif arg_command == config.arg_command_featureSelection:
        featureSelection(arg_input)
    elif arg_command == config.arg_command_performModelExecution:
        performModelExecution(arg_input, arg_subset, arg_type, arg_model)
    else:
        sys.exit(1)