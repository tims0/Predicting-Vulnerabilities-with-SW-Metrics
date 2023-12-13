import logging
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config
from feature_selection import featureSelection
from data_preprocessing import preprocessFileDataset, preprocessFileDataset_understand

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "featureSelection_understand.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def create_or_load_cfs_understand_dataset(file, label):
    if preprocessFileDataset.check_if_file_exists(file):
        dataset = preprocessFileDataset.load_json_file(file)
    else:
        dataset_original = preprocessFileDataset_understand.create_or_load_necessary_understand_dataset()
        dataset = featureSelection.prepare_feature_selection(dataset_original)
        
        subset, value = featureSelection.performFeatureSelection(dataset, label, config.max_backtrack)
        dataset = featureSelection.createSelectedDataset(dataset_original, subset, label)
        preprocessFileDataset.store_dataset_to_json(dataset, file)
    
    return dataset

def preprocess_selected_understand_dataset_vul():
    dataset = create_or_load_cfs_understand_dataset(config.understand_dataset_cfs_vul, config.column_vul)

    # Split it into train, test and validation data
    train, test, val = preprocessFileDataset.split_dataset(dataset)

    # Splitting train, test and validation data into features and target variables
    x_train, y_train = preprocessFileDataset.split_attributes_cfs(train)
    x_test, y_test = preprocessFileDataset.split_attributes_cfs(test)
    x_val, y_val = preprocessFileDataset.split_attributes_cfs(val)

    # Performing feature scaling for all feature sets
    x_train = preprocessFileDataset.feature_scaling(x_train)
    x_test = preprocessFileDataset.feature_scaling(x_test)
    x_val = preprocessFileDataset.feature_scaling(x_val)

    # Storing data into csv files for further processing
    preprocessFileDataset.store_data_to_csv(x_train, config.understand_cfs_vul_files['x_train'])
    preprocessFileDataset.store_data_to_csv(y_train, config.understand_cfs_vul_files['y_train'])
    preprocessFileDataset.store_data_to_csv(x_test, config.understand_cfs_vul_files['x_test'])
    preprocessFileDataset.store_data_to_csv(y_test, config.understand_cfs_vul_files['y_test'])
    preprocessFileDataset.store_data_to_csv(x_val, config.understand_cfs_vul_files['x_val'])
    preprocessFileDataset.store_data_to_csv(y_val, config.understand_cfs_vul_files['y_val'])

def preprocess_selected_understand_dataset_score():
    dataset = create_or_load_cfs_understand_dataset(config.understand_dataset_cfs_vul, config.column_vul)

    # Split it into train, test and validation data
    train, test, val = preprocessFileDataset.split_dataset(dataset)

    # Splitting train, test and validation data into features and target variables
    x_train, y_train = preprocessFileDataset.split_attributes_cfs(train)
    x_test, y_test = preprocessFileDataset.split_attributes_cfs(test)
    x_val, y_val = preprocessFileDataset.split_attributes_cfs(val)

    # Performing feature scaling for all feature sets
    x_train = preprocessFileDataset.feature_scaling(x_train)
    x_test = preprocessFileDataset.feature_scaling(x_test)
    x_val = preprocessFileDataset.feature_scaling(x_val)

    # Storing data into csv files for further processing
    preprocessFileDataset.store_data_to_csv(x_train, config.understand_cfs_score_files['x_train'])
    preprocessFileDataset.store_data_to_csv(y_train, config.understand_cfs_score_files['y_train'])
    preprocessFileDataset.store_data_to_csv(x_test, config.understand_cfs_score_files['x_test'])
    preprocessFileDataset.store_data_to_csv(y_test, config.understand_cfs_score_files['y_test'])
    preprocessFileDataset.store_data_to_csv(x_val, config.understand_cfs_score_files['x_val'])
    preprocessFileDataset.store_data_to_csv(y_val, config.understand_cfs_score_files['y_val'])

def perform_understand_feature_selection():
    preprocess_selected_understand_dataset_vul()
    preprocess_selected_understand_dataset_score()