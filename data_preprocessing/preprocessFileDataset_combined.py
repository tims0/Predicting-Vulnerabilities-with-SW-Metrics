import pandas as pd
from sqlite3 import Error
import logging
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config
from data_preprocessing import preprocessFileDataset

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "preprocessFileDataset_combined.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

# Getting all needed file informations
def get_all_file_informations(conn):
    query_dataset_metrics_understand = "SELECT * FROM file_metrics_understand"
    query_dataset_metrics_analizo = "SELECT * FROM file_metrics_analizo"
    query_dataset_files = "SELECT file_change.file_change_id, file_change.hash, file_change.programming_language FROM file_change"
    query_dataset_cve_cwe = "SELECT fixes.repo_url, fixes.hash, cve.cvss2_base_score, cve.cvss3_base_score, cwe.cwe_id, cwe.cwe_name FROM fixes, cve, cwe_classification, cwe WHERE fixes.cve_id = cve.cve_id AND cve.cve_id = cwe_classification.cve_id AND cwe_classification.cwe_id = cwe.cwe_id"

    logging.info("Executing the database file query..")
    try:
        dataset_metrics_understand = pd.read_sql(query_dataset_metrics_understand, conn)
        dataset_metrics_analizo = pd.read_sql(query_dataset_metrics_analizo, conn)
        dataset_files = pd.read_sql(query_dataset_files, conn)
        dataset_cve_cwe = pd.read_sql(query_dataset_cve_cwe, conn)
        logging.info("Execution of queries successful.")
    except Error as e:
        logging.error("Database error: Database execution of queries failed!")
        logging.error(e)
        sys.exit(1)
    
    dataset = dataset_metrics_understand.merge(dataset_metrics_analizo, how='left', left_on=['file_change_id', 'before_change'], right_on=['file_change_id', 'before_change'])
    dataset = dataset.merge(dataset_files, how='left', on='file_change_id')
    dataset = dataset.merge(dataset_cve_cwe, how='left', on='hash')

    return dataset

# Clean dataframe of all columns with no informations
def clean_combined_dataset_with_all_informations(dataset):
    return dataset.drop(columns=['CountDeclInstanceVariablePrivate', 'CountDeclInstanceVariableInternal', 'CountDeclMethodFriend', 'CountDeclMethodAll', 'PercentLackOfCohesionModified', 
                                'CountDeclFile', 'CountDeclInstanceVariableProtectedInternal', 'AvgEssentialStrictModified', 'EssentialStrictModified', 'SumEssentialStrictModified', 
                                'CountOutput', 'PercentLackOfCohesion', 'CountClassCoupledModified', 'CountDeclInstanceVariablePublic', 'MaxInheritanceTree', 'CountDeclInstanceVariableProtected', 
                                'CountDeclMethodInternal', 'CountDeclSubprogram', 'Knots', 'CountDeclMethodConst', 'CountDeclLibunit', 'CountClassBase', 'CountDeclMethodProtectedInternal', 
                                'CountDeclMethodStrictPrivate', 'CountPackageCoupled', 'CountInput', 'MaxEssentialKnots', 'CountDeclFileCode', 'CountDeclPropertyAuto', 'MaxEssentialStrictModified', 
                                'CountDeclFileHeader', 'CountDeclProperty', 'CountClassCoupled', 'CountDeclModule', 'MinEssentialKnots', 'CountDeclMethodStrictPublished', 'CountClassDerived', 
                                '_filename', '_module', 'acc', 'cbo', 'noc', 'sc'])

# Setup all informations in one dataframe and store it as json file
def create_combined_dataset_with_all_informations(conn):
    logging.info("Creating dataset with all informations..")
    dataset = get_all_file_informations(conn)
    dataset = clean_combined_dataset_with_all_informations(dataset)
    preprocessFileDataset.store_dataset_to_json(dataset, config.combined_dataset_all)
    logging.info("Dataset creation with all informations finished.")

    return dataset

# Setup all necessary informations in one dataframe and store it as json file
def create_combined_dataset_with_necessary_informations(conn):
    if preprocessFileDataset.check_if_file_exists(config.combined_dataset_all):
        dataset = preprocessFileDataset.load_json_file(config.combined_dataset_all)
    else:
        dataset = create_combined_dataset_with_all_informations(conn)

    logging.info("Creating dataset with necessary informations..")
    dataset = dataset.drop(columns=['file_change_id', 'Kind', 'Name', 'hash', 'cwe_id', 'cwe_name', 'cvss2_base_score'])
    temp_cols = dataset.columns.tolist()
    new_cols = temp_cols[1:] + temp_cols[0:1]
    dataset = dataset[new_cols]
    dataset = dataset[dataset['cvss3_base_score']!='nan']

    dataset = preprocessFileDataset.convert_before_change(dataset)
    dataset = preprocessFileDataset.encode_programming_language(dataset)
    preprocessFileDataset.store_dataset_to_json(dataset, config.combined_dataset_necessary)
    logging.info("Dataset creation with necessary informations finished.")

    return dataset

def create_or_load_necessary_combined_dataset():
    # Create dataset with necessary informations
    if preprocessFileDataset.check_if_file_exists(config.combined_dataset_necessary):
        dataset = preprocessFileDataset.load_json_file(config.combined_dataset_necessary)
    else:
        conn = preprocessFileDataset.create_db_connection(config.db_file)
        dataset = create_combined_dataset_with_necessary_informations(conn)
    
    return dataset

# Preprocess the dataset and store all training, test and validation data in csv files
def preprocess_combined_dataset():
    dataset = create_or_load_necessary_combined_dataset()

    # Replace missing values in dataset and split it into train, test and validation data
    dataset = preprocessFileDataset.replace_missing_values(dataset)
    train, test, val = preprocessFileDataset.split_dataset(dataset)

    # Splitting train, test and validation data into features and target variables
    x_train, y_train = preprocessFileDataset.split_attributes(train)
    x_test, y_test = preprocessFileDataset.split_attributes(test)
    x_val, y_val = preprocessFileDataset.split_attributes(val)

    # Performing feature scaling for all feature sets
    x_train = preprocessFileDataset.feature_scaling(x_train)
    x_test = preprocessFileDataset.feature_scaling(x_test)
    x_val = preprocessFileDataset.feature_scaling(x_val)

    # Storing data into csv files for further processing
    preprocessFileDataset.store_data_to_csv(x_train, config.combined_csv_files['x_train'])
    preprocessFileDataset.store_data_to_csv(y_train, config.combined_csv_files['y_train'])
    preprocessFileDataset.store_data_to_csv(x_test, config.combined_csv_files['x_test'])
    preprocessFileDataset.store_data_to_csv(y_test, config.combined_csv_files['y_test'])
    preprocessFileDataset.store_data_to_csv(x_val, config.combined_csv_files['x_val'])
    preprocessFileDataset.store_data_to_csv(y_val, config.combined_csv_files['y_val'])
