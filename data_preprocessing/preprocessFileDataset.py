import logging
import numpy as np # used for handling numbers
import os
import pandas as pd # used for handling the dataset
from sklearn.impute import SimpleImputer # used for handling missing data
from sklearn.preprocessing import OneHotEncoder # used for encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GroupShuffleSplit # used for splitting training and testing data
from sklearn.preprocessing import MinMaxScaler # used for feature scaling
import sqlite3
from sqlite3 import Error
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "preprocessFileDataset.log", 
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

# Getting all needed file informations
def get_all_file_informations(conn, metrics_table):
    query_dataset_metrics = "SELECT * FROM " + metrics_table
    query_dataset_files = "SELECT file_change.file_change_id, file_change.hash, file_change.programming_language FROM file_change"
    query_dataset_cve_cwe = "SELECT fixes.repo_url, fixes.hash, cve.cvss2_base_score, cve.cvss3_base_score, cwe.cwe_id, cwe.cwe_name FROM fixes, cve, cwe_classification, cwe WHERE fixes.cve_id = cve.cve_id AND cve.cve_id = cwe_classification.cve_id AND cwe_classification.cwe_id = cwe.cwe_id"

    logging.info("Executing the database method query..")
    try:
        dataset_metrics = pd.read_sql(query_dataset_metrics, conn)
        dataset_files = pd.read_sql(query_dataset_files, conn)
        dataset_cve_cwe = pd.read_sql(query_dataset_cve_cwe, conn)
        logging.info("Execution of queries successful.")
    except Error as e:
        logging.error("Database error: Database execution of queries failed!")
        logging.error(e)
        sys.exit(1)
    
    dataset = dataset_metrics.merge(dataset_files, how='left', on='file_change_id')
    dataset = dataset.merge(dataset_cve_cwe, how='left', on='hash')
    return dataset

# Check if file already exists
def check_if_file_exists(file):
    if os.path.exists(file):
        return True
    return False

# Loading file from JSON as DataFrame
def load_json_file(file):
    return pd.read_json(file)

# Storing datasets as json files
def store_dataset_to_json(dataset, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    dataset.to_json(filename, orient="records", indent=4)

# Converting values from before_change to 0 (False) and 1 (True)
def convert_before_change(dataset):
    dataset.loc[dataset['before_change'] == 'False', 'cvss3_base_score'] =  0
    dataset.loc[dataset['before_change'] == 'False', 'before_change'] =  0
    dataset.loc[dataset['before_change'] == 'True', 'before_change'] =  1

    return dataset

# Encode categorical data for programming_language
def encode_programming_language(dataset):
    columntransformer = ColumnTransformer([("", OneHotEncoder(sparse_output=False), ['programming_language'])], remainder = 'passthrough')
    columntransformer.set_output(transform="pandas")
    dataset = columntransformer.fit_transform(dataset)

    return dataset

# Handling the missing data and replace missing values with nan from numpy and replace with 0 of all the other values
def replace_missing_values(dataset):
    imputer_dataset = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0)
    imputer_dataset = imputer_dataset.fit(dataset)
    dataset = pd.DataFrame(imputer_dataset.transform(dataset), columns=dataset.columns)

    return dataset

# Splitting the dataset into training, test and validation set
def split_dataset(dataset):
    splitter = GroupShuffleSplit(test_size=.40, n_splits=2, random_state = 7)
    split = splitter.split(dataset, groups=dataset[config.column_repo_url])
    train_inds, test_val_inds = next(split)

    train = dataset.iloc[train_inds]
    train = train.drop(columns=[config.column_repo_url])
    test_val = dataset.iloc[test_val_inds]
    test_val = test_val.reset_index(drop=True)

    splitter2 = GroupShuffleSplit(test_size=.50, n_splits=2, random_state = 7)
    split2 = splitter2.split(test_val, groups=test_val[config.column_repo_url])
    test_inds, val_inds = next(split2)

    test = test_val.iloc[test_inds]
    test = test.drop(columns=[config.column_repo_url])
    val = test_val.iloc[val_inds]
    val = val.drop(columns=[config.column_repo_url])

    return train, test, val

# Splitting the attributes into independent and dependent attributes
def split_attributes(dataset):
    x_dataset = dataset.iloc[:, :-2] # attributes to determine dependent variable / Class; all columns of data frame excepting the last columns
    y_dataset = dataset.iloc[:, -2:] # dependent variable / Class; last columns of data frame

    return x_dataset, y_dataset

# Splitting the attributes into independent and dependent attributes
def split_attributes_cfs(dataset):
    x_dataset = dataset.iloc[:, :-1] # attributes to determine dependent variable / Class; all columns of data frame excepting the last columns
    y_dataset = dataset.iloc[:, -1:] # dependent variable / Class; last columns of data frame

    return x_dataset, y_dataset

# Feature scaling for independent attributes
def feature_scaling(x_dataset):
    mms_X = MinMaxScaler()
    x_dataset_columns = x_dataset.columns
    x_dataset = pd.DataFrame(mms_X.fit_transform(x_dataset), columns=x_dataset_columns)

    return x_dataset

# Storing splittet parts of datasets as csv files
def store_data_to_csv(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data.to_csv(filename, sep=',', index=False)