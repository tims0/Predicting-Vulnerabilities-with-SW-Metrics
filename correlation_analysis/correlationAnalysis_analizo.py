import logging
import seaborn as sns
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config
from correlation_analysis import correlationAnalysis
from data_preprocessing import preprocessFileDataset, preprocessFileDataset_analizo

sns.set(rc={'figure.figsize':(125,125)})
os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "correlationAnalysis_analizo.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def get_analizo_dataset():
    if preprocessFileDataset.check_if_file_exists(config.analizo_dataset_necessary):
        return preprocessFileDataset.load_json_file(config.analizo_dataset_necessary)
    else:
        conn = preprocessFileDataset.create_db_connection(config.db_file)
        return preprocessFileDataset_analizo.create_analizo_dataset_with_necessary_informations(conn)

def perform_correalation_analysis_and_tests():
    dataset = get_analizo_dataset()
    correlationAnalysis.perform_all_correlation_analysis(dataset, config.analizo_correlation_files)
    correlationAnalysis.perform_all_tests(dataset, config.correlation_threshold, config.analizo_correlation_files)
