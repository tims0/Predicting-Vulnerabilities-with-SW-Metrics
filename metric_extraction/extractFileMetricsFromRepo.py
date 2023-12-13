import logging
import os
import pandas as pd
import shutil
import sqlite3
from sqlite3 import Error
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "extractFileMetricsFromRepo.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

# Creating database connection to SQLite3 with database file db_file; returning connection
def create_db_connection(db_file):
    try:
        conn = sqlite3.connect(db_file, timeout=10)
        logging.info("Connection to database successful.")

        return conn
    except Error as e:
        logging.error("Database error: Failed to connect to database!")
        logging.error(e)
        sys.exit(1)

# Getting informations (filechange_id, file name, code_before, code_after) for every filechange record in CVEfixes; returning cursor of the result
def get_file_informations(conn):
    query_file_informations = "SELECT file_change_id, filename, code_after, code_before FROM file_change"
    cursor = conn.cursor()
    try:
        cursor.execute(query_file_informations)
        logging.info("Execution of file query successful.")

        return cursor
    except Error as e:
        logging.error("Database error: Database execution of file query failed!")
        logging.error(e)
        sys.exit(1)

# Getting already processed metrics for specified metrics_table and returning as pandas dataframe
def get_processsed_metrics(conn, metrics_table):
    cursor = conn.cursor()

    query_metrics_table_exists = "SELECT * FROM " + metrics_table
    query_select_metrics = "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='" + metrics_table + "'"

    try:
        cursor.execute(query_metrics_table_exists)
        if cursor.fetchone()[0] > 0:
            df_sql = pd.read_sql_query(query_select_metrics, conn)
        else:
            df_sql = pd.DataFrame()
        logging.info("Execution of metrics query successful.")

        return df_sql
    except Error as e:
        logging.error("Database error: Database execution of metrics query failed!")
        logging.error(e)
        sys.exit(1)

# Skipping already processed metrics in the cursor of files to return cursor on position for further metric processing
def skip_processed_metrics(cursor, df_sql, file_id_sql_col):
    if not df_sql.empty:
        last_file_change_id = df_sql.iloc[-1, df_sql.columns.get_loc(file_id_sql_col)]
        while True:
            result = cursor.fetchone()
            if result[0] == last_file_change_id:
                break
            else:
                logging.info("Skipping file with ID %s", result[0])
    return cursor

# Creating path, if it not exists and clearing all files and folders inside this path
def clear_path_or_create(path):
    if os.path.exists(path):
        shutil.remtree(path)
    os.makedirs(path)

# Writing a file with filename in path with code as content
def write_file(path, filename, code):
    clear_path_or_create(path)
    with open(path + "/" + filename, "w") as file:
        file.write(code)

def clear_path_and_write_file(path, filename, code):
    clear_path_or_create(path)
    write_file(path, filename, code)

def insert_metrics_to_database(conn, metrics_table, df_metrics, file_id):
    # Inserting extracted metrics in database
    try:
        df_metrics = df_metrics.applymap(str)
        df_metrics.to_sql(name=metrics_table, con=conn, if_exists="append", index=False)
        conn.commit()
        logging.info("Successfully inserting extracted metrics from file with ID %s into database table", file_id)
    except Error as e:
        logging.error("Database error: Could not insert extracted metrics from file with ID %s into database table!", file_id)
        logging.error(e)
        sys.exit(1)