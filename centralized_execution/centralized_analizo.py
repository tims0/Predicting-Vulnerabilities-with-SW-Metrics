import logging
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config
from centralized_execution import centralized

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "centralized_analizo.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)


def performAnalizoAllVul(model_path, filename):
    x_train, y_train, x_test, y_test, x_val, y_val = centralized.getAllData(config.analizo_csv_files)

    y_train = y_train.iloc[:, -1:]
    y_test = y_test.iloc[:, -1:]
    y_val = y_val.iloc[:, -1:]

    model = centralized.getVulModel(model_path)

    estimator = centralized.getScoreEstimator(model, x_train, y_train)

    initial_history = centralized.trainScoreModel(estimator, x_train, y_train, x_val, y_val)

    centralized.predictAndEvaluateScoreModel(estimator, initial_history, filename, x_train, y_train, x_test, y_test, x_val, y_val)

def performAnalizoAllScore(model_path, filename):
    x_train, y_train, x_test, y_test, x_val, y_val = centralized.getAllData(config.analizo_csv_files)

    y_train = y_train.iloc[:, 0]
    y_test = y_test.iloc[:, 0]
    y_val = y_val.iloc[:, 0]

    model = centralized.getScoreModel(model_path)

    initial_history = centralized.trainScoreModel(model, x_train, y_train, x_val, y_val)

    centralized.predictAndEvaluateScoreModel(model, initial_history, filename, x_train, y_train, x_test, y_test, x_val, y_val)

def performAnalizoCFSVul(model_path, filename):
    x_train, y_train, x_test, y_test, x_val, y_val = centralized.getAllData(config.analizo_cfs_vul_files)
    model = centralized.getVulModel(model_path)
    initial_history = centralized.trainVulModel(model, x_train, y_train, x_val, y_val)
    centralized.predictAndEvaluateVulModel(model, initial_history, filename, x_train, y_train, x_test, y_test, x_val, y_val)

def performAnalizoCFSScore(model_path, filename):
    x_train, y_train, x_test, y_test, x_val, y_val = centralized.getAllData(config.analizo_cfs_score_files)
    model = centralized.getScoreModel(model_path)
    estimator = centralized.getScoreEstimator(model, x_train, y_train)
    initial_history = centralized.trainScoreModel(estimator, x_train, y_train, x_val, y_val)
    centralized.predictAndEvaluateScoreModel(estimator, initial_history, filename, x_train, y_train, x_test, y_test, x_val, y_val)
