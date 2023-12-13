import logging
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config
from models import models
from data_preprocessing import preprocessFileDataset_combined
from correlation_analysis import correlationAnalysis_combined
from feature_selection import featureSelection_combined
from centralized_execution import centralized_combined

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "combined.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def preprocessFileDatasetCombined():
    preprocessFileDataset_combined.preprocess_combined_dataset()

def correlationAnalysisCombined():
    correlationAnalysis_combined.perform_correalation_analysis_and_tests()

def featureSelectionCombined():
    featureSelection_combined.perform_combined_feature_selection()

def performCombinedAllVulS():
    models.createAndSaveModelS(config.combined_all_models["input"], config.combined_all_models["S_Path"])
    centralized_combined.performCombinedAllVul(config.combined_all_models["S_Path"], config.combined_all_s)

def performCombinedAllVulM():
    models.createAndSaveModelM(config.combined_all_models["input"], config.combined_all_models["M_Path"])
    centralized_combined.performCombinedAllVul(config.combined_all_models["M_Path"], config.combined_all_m)

def performCombinedAllVulL():
    models.createAndSaveModelL(config.combined_all_models["input"], config.combined_all_models["L_Path"])
    centralized_combined.performCombinedAllVul(config.combined_all_models["L_Path"], config.combined_all_l)

def performCombinedAllScoreS():
    models.createAndSaveModelS(config.combined_all_models["input"], config.combined_all_models["S_Path"])
    centralized_combined.performCombinedAllScore(config.combined_all_models["S_Path"], config.combined_all_s)

def performCombinedAllScoreM():
    models.createAndSaveModelM(config.combined_all_models["input"], config.combined_all_models["M_Path"])
    centralized_combined.performCombinedAllScore(config.combined_all_models["M_Path"], config.combined_all_m)

def performCombinedAllScoreL():
    models.createAndSaveModelL(config.combined_all_models["input"], config.combined_all_models["L_Path"])
    centralized_combined.performCombinedAllScore(config.combined_all_models["L_Path"], config.combined_all_l)

def performCombinedCFSVulS():
    models.createAndSaveModelS(config.combined_cfs_vul_models["input"], config.combined_cfs_vul_models["S_Path"])
    centralized_combined.performCombinedCFSVul(config.combined_all_models["S_Path"], config.combined_cfs_s)

def performCombinedCFSVulM():
    models.createAndSaveModelM(config.combined_cfs_vul_models["input"], config.combined_cfs_vul_models["M_Path"])
    centralized_combined.performCombinedCFSVul(config.combined_all_models["M_Path"], config.combined_cfs_m)

def performCombinedCFSVulL():
    models.createAndSaveModelL(config.combined_cfs_vul_models["input"], config.combined_cfs_vul_models["L_Path"])
    centralized_combined.performCombinedCFSVul(config.combined_all_models["L_Path"], config.combined_cfs_l)

def performCombinedCFSScoreS():
    models.createAndSaveModelS(config.combined_cfs_score_models["input"], config.combined_cfs_score_models["S_Path"])
    centralized_combined.performCombinedCFSScore(config.combined_all_models["S_Path"], config.combined_cfs_s)

def performCombinedCFSScoreM():
    models.createAndSaveModelM(config.combined_cfs_score_models["input"], config.combined_cfs_score_models["M_Path"])
    centralized_combined.performCombinedCFSScore(config.combined_all_models["M_Path"], config.combined_cfs_m)

def performCombinedCFSScoreL():
    models.createAndSaveModelL(config.combined_cfs_score_models["input"], config.combined_cfs_score_models["L_Path"])
    centralized_combined.performCombinedCFSScore(config.combined_all_models["L_Path"], config.combined_cfs_l)

def performCombinedAllVul(model):
    if model == config.arg_model_l:
        performCombinedAllVulL()
    elif model == config.arg_model_m:
        performCombinedAllVulM()
    elif model == config.arg_model_s:
        performCombinedAllVulS()
    elif model == config.arg_all:
        performCombinedAllVulS()
        performCombinedAllVulM()
        performCombinedAllVulL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performCombinedAllScore(model):
    if model == config.arg_model_l:
        performCombinedAllScoreL()
    elif model == config.arg_model_m:
        performCombinedAllScoreM()
    elif model == config.arg_model_s:
        performCombinedAllScoreS()
    elif model == config.arg_all:
        performCombinedAllScoreS()
        performCombinedAllScoreM()
        performCombinedAllScoreL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performCombinedCFSVul(model):
    if model == config.arg_model_l:
        performCombinedCFSVulL()
    elif model == config.arg_model_m:
        performCombinedCFSVulM()
    elif model == config.arg_model_s:
        performCombinedCFSVulS()
    elif model == config.arg_all:
        performCombinedCFSVulS()
        performCombinedCFSVulM()
        performCombinedCFSVulL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performCombinedCFSScore(model):
    if model == config.arg_model_l:
        performCombinedCFSScoreL()
    elif model == config.arg_model_m:
        performCombinedCFSScoreM()
    elif model == config.arg_model_s:
        performCombinedCFSScoreS()
    elif model == config.arg_all:
        performCombinedCFSScoreS()
        performCombinedCFSScoreM()
        performCombinedCFSScoreL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performCombinedAll(type, model):
    if type == config.arg_type_vul:
        performCombinedAllVul(model)
    elif type == config.arg_type_score:
        performCombinedAllScore(model)
    elif type == config.arg_all:
        performCombinedAllVul(model)
        performCombinedAllScore(model)
    else:
        logging.error("Agrument Error - Please use vul, score or all as argument for type")

def performCombinedCFS(type, model):
    if type == config.arg_type_vul:
        performCombinedCFSVul(model)
    elif type == config.arg_type_score:
        performCombinedCFSScore(model)
    elif type == config.arg_all:
        performCombinedCFSVul(model)
        performCombinedCFSScore(model)
    else:
        logging.error("Agrument Error - Please use vul, score or all as argument for type")

def performCombined(subset, type, model):
    if subset == config.arg_subset_all:
        performCombinedAll(type, model)
    elif subset == config.arg_subset_cfs:
        performCombinedCFS(type, model)
    elif subset == config.arg_subset_both:
        performCombinedAll(type, model)
        performCombinedCFS(type, model)
    else:
        logging.error("Argument Error - Please use cfs, both or all as argument for subset")
