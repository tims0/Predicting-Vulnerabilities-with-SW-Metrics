import logging
import os
import pandas as pd
import subprocess
import sys
import yaml

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config
from metric_extraction import extractFileMetricsFromRepo

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "extractFileMetricsFromRepo_analizo.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def createAnalizoMetrics(path):
    # Creating analizo project + analyzing the repo via CLI + reporting the metrics as yaml file
    logging.info("Creating analizo metrics from the file for metric extraction..")
    try:
        output = subprocess.check_output(
            "analizo metrics --output {yaml_file} {repo_path}".format(yaml_file=config.yaml_file, repo_path=path),
            shell=True, timeout=30)
        logging.debug(output)
    except subprocess.CalledProcessError as e:
        logging.error(e.output)
        logging.warning("analizo creation failed")
    except subprocess.TimeoutExpired as e:
        logging.error(e.output)
        logging.warning("analizo creation timeout")

def extractAnalizoMetricsFromCsvFile(conn, file_id, filename):
    # Querying the yaml file for metric extraction
    if os.path.exists(config.yaml_file):
        curr_yaml_file = config.yaml_file
        with open(curr_yaml_file) as curr_yaml_file:
            yaml_contents = list(yaml.load_all(curr_yaml_file, Loader=yaml.FullLoader))

        if yaml_contents and len(yaml_contents) == 2:
            yaml_df = pd.json_normalize(yaml_contents[1])
            yaml_df.insert(0, config.file_id_sql_col, [file_id])
            yaml_df.insert(1, "before_change", ["False"])
            logging.info("Found unique match for file with name %s and ID %s after change in analizo", filename, file_id)

            extractFileMetricsFromRepo.insert_metrics_to_database(conn, config.analizo_metrics_table, yaml_df, file_id)
            yaml_df = yaml_df[0:0]
        else:
            if not yaml_contents or len(yaml_contents) < 2:
                logging.warning("Could not match file with name %s and ID %s after change in analizo", filename, file_id)
            if len(yaml_contents) > 2:
                logging.warning("Found two many matches for file with name %s for ID %s after change in analizo", filename, file_id)

def extractAnalizoMetrics(conn, path, file_id, filename, code):
    extractFileMetricsFromRepo.clear_path_and_write_file(path, filename, code)
    createAnalizoMetrics(path)
    extractAnalizoMetricsFromCsvFile(conn, file_id, filename)

def extractAnalizoMetricsFromRepo():
    # Create database connection (1), getting file informations (2) and all already processed metrics (3) to skip these (4)
    conn = extractFileMetricsFromRepo.create_db_connection(config.db_file)
    cursor = extractFileMetricsFromRepo.get_file_informations(conn)
    df_sql = extractFileMetricsFromRepo.get_processsed_metrics(conn, config.understand_metrics_table)
    cursor = extractFileMetricsFromRepo.skip_processed_metrics(df_sql, config.file_id_sql_col)

    # Fetching database entries
    while True:
        result = cursor.fetchone()

        # End loop until metrics for all file entries are processed
        if not result or result is None:
            logging.info("All entries processed.")
            break

        # Assigning values from entry in variables
        file_id = result[0]
        filename = result[1]
        code_after = result[2]
        code_before = result[3]

        # Processing metrics for file after modifications when it wasn't deleted
        if not code_after == "None":
            # Putting code_after in seperate file for metric processing with understand
            logging.info("Writing code after modifications into file with name %s", filename)
            extractAnalizoMetrics(conn, config.repo_path, file_id, filename, code_after)

        # Processing metrics for file before modifications when it already existed
        if not code_before == "None":
            # Putting code_before in seperate file for metric processing with understand
            logging.info("Writing code before modifications into file with name %s", filename)
            extractAnalizoMetrics(conn, config.repo_path, file_id, filename, code_before)

    logging.info("Metric processing finished (end of file).")