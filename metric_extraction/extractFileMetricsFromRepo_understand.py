import logging
import os
import pandas as pd
import subprocess
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config
from metric_extraction import extractFileMetricsFromRepo

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "extractFileMetricsFromRepo_understand.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def createUnderstandMetrics(path):
    # Creating understand project + analyzing the repo via CLI + reporting the metrics as csv file
    logging.info("Creating understand project from the file for metric extraction..")
    try:
        output = subprocess.check_output(
            "und create -db {udb_file} create -languages all add {repo_path} analyze metrics".format(udb_file=config.udb_file, repo_path=path),
            shell=True, timeout=300)
        logging.debug(output)
    except subprocess.CalledProcessError as e:
        logging.error(e.output)
        logging.warning("udb creation failed")
    except subprocess.TimeoutExpired as e:
        logging.error(e.output)
        logging.warning("udb creation timeout")

def extractUnderstandMetricsFromCsvFile(conn, file_id, filename):
    # Querying the csv file for metric extraction
    if os.path.exists(config.csv_file):
        df_csv = pd.read_csv(config.csv_file, on_bad_lines='skip')
        df_row = df_csv[df_csv['Name']==filename]
        if not df_row.empty and len(df_row.index) == 1:
            df_row.insert(0, config.file_id_sql_col, [file_id])
            df_row.insert(1, "before_change", ["False"])
            logging.info("Found unique match for file with name %s and ID %s in understand project", filename, file_id)

            extractFileMetricsFromRepo.insert_metrics_to_database(conn, config.understand_metrics_table, df_row, file_id)
            df_row = df_row[0:0]
        else:
            if df_row.empty:
                logging.warning("Could not match file with name %s and ID %s in understand project", filename, file_id)
            if len(df_row.index) > 1:
                logging.warning("Found two many matches for file with name %s for ID %s in understand project", filename, file_id)

def extractUnderstandMetrics(conn, path, file_id, filename, code):
    extractFileMetricsFromRepo.clear_path_and_write_file(path, filename, code)
    createUnderstandMetrics(path)
    extractUnderstandMetricsFromCsvFile(conn, file_id, filename)

def extractUnderstandMetricsFromRepo():
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
            extractUnderstandMetrics(conn, config.repo_path, file_id, filename, code_after)

        # Processing metrics for file before modifications when it already existed
        if not code_before == "None":
            # Putting code_before in seperate file for metric processing with understand
            logging.info("Writing code before modifications into file with name %s", filename)
            extractUnderstandMetrics(conn, config.repo_path, file_id, filename, code_before)

    logging.info("Metric processing finished (end of file).")