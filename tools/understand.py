import logging
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config
from models import models
from metric_extraction import extractFileMetricsFromRepo_understand
from data_preprocessing import preprocessFileDataset_understand
from correlation_analysis import correlationAnalysis_understand
from feature_selection import featureSelection_understand
from centralized_execution import centralized_understand

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "understand.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def extractFileMetricsFromRepoUnderstand():
    extractFileMetricsFromRepo_understand.extractUnderstandMetricsFromRepo()

def preprocessFileDatasetUnderstand():
    preprocessFileDataset_understand.preprocess_understand_dataset()

def correlationAnalysisUnderstand():
    correlationAnalysis_understand.perform_correalation_analysis_and_tests()

def featureSelectionUnderstand():
    featureSelection_understand.perform_understand_feature_selection()

def performUnderstandAllVulS():
    models.createAndSaveModelS(config.understand_all_models["input"], config.understand_all_models["S_Path"])
    centralized_understand.performUnderstandAllVul(config.understand_all_models["S_Path"], config.understand_all_s)

def performUnderstandAllVulM():
    models.createAndSaveModelM(config.understand_all_models["input"], config.understand_all_models["M_Path"])
    centralized_understand.performUnderstandAllVul(config.understand_all_models["M_Path"], config.understand_all_m)

def performUnderstandAllVulL():
    models.createAndSaveModelL(config.understand_all_models["input"], config.understand_all_models["L_Path"])
    centralized_understand.performUnderstandAllVul(config.understand_all_models["L_Path"], config.understand_all_l)

def performUnderstandAllScoreS():
    models.createAndSaveModelS(config.understand_all_models["input"], config.understand_all_models["S_Path"])
    centralized_understand.performUnderstandAllScore(config.understand_all_models["S_Path"], config.understand_all_s)

def performUnderstandAllScoreM():
    models.createAndSaveModelM(config.understand_all_models["input"], config.understand_all_models["M_Path"])
    centralized_understand.performUnderstandAllScore(config.understand_all_models["M_Path"], config.understand_all_m)

def performUnderstandAllScoreL():
    models.createAndSaveModelL(config.understand_all_models["input"], config.understand_all_models["L_Path"])
    centralized_understand.performUnderstandAllScore(config.understand_all_models["L_Path"], config.understand_all_l)

def performUnderstandCFSVulS():
    models.createAndSaveModelS(config.understand_cfs_vul_models["input"], config.understand_cfs_vul_models["S_Path"])
    centralized_understand.performUnderstandCFSVul(config.understand_all_models["S_Path"], config.understand_cfs_s)

def performUnderstandCFSVulM():
    models.createAndSaveModelM(config.understand_cfs_vul_models["input"], config.understand_cfs_vul_models["M_Path"])
    centralized_understand.performUnderstandCFSVul(config.understand_all_models["M_Path"], config.understand_cfs_m)

def performUnderstandCFSVulL():
    models.createAndSaveModelL(config.understand_cfs_vul_models["input"], config.understand_cfs_vul_models["L_Path"])
    centralized_understand.performUnderstandCFSVul(config.understand_all_models["L_Path"], config.understand_cfs_l)

def performUnderstandCFSScoreS():
    models.createAndSaveModelS(config.understand_cfs_score_models["input"], config.understand_cfs_score_models["S_Path"])
    centralized_understand.performUnderstandCFSScore(config.understand_all_models["S_Path"], config.understand_cfs_s)

def performUnderstandCFSScoreM():
    models.createAndSaveModelM(config.understand_cfs_score_models["input"], config.understand_cfs_score_models["M_Path"])
    centralized_understand.performUnderstandCFSScore(config.understand_all_models["M_Path"], config.understand_cfs_m)

def performUnderstandCFSScoreL():
    models.createAndSaveModelL(config.understand_cfs_score_models["input"], config.understand_cfs_score_models["L_Path"])
    centralized_understand.performUnderstandCFSScore(config.understand_all_models["L_Path"], config.understand_cfs_l)

def performUnderstandAllVul(model):
    if model == config.arg_model_l:
        performUnderstandAllVulL()
    elif model == config.arg_model_m:
        performUnderstandAllVulM()
    elif model == config.arg_model_s:
        performUnderstandAllVulS()
    elif model == config.arg_all:
        performUnderstandAllVulS()
        performUnderstandAllVulM()
        performUnderstandAllVulL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performUnderstandAllScore(model):
    if model == config.arg_model_l:
        performUnderstandAllScoreL()
    elif model == config.arg_model_m:
        performUnderstandAllScoreM()
    elif model == config.arg_model_s:
        performUnderstandAllScoreS()
    elif model == config.arg_all:
        performUnderstandAllScoreS()
        performUnderstandAllScoreM()
        performUnderstandAllScoreL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performUnderstandCFSVul(model):
    if model == config.arg_model_l:
        performUnderstandCFSVulL()
    elif model == config.arg_model_m:
        performUnderstandCFSVulM()
    elif model == config.arg_model_s:
        performUnderstandCFSVulS()
    elif model == config.arg_all:
        performUnderstandCFSVulS()
        performUnderstandCFSVulM()
        performUnderstandCFSVulL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performUnderstandCFSScore(model):
    if model == config.arg_model_l:
        performUnderstandCFSScoreL()
    elif model == config.arg_model_m:
        performUnderstandCFSScoreM()
    elif model == config.arg_model_s:
        performUnderstandCFSScoreS()
    elif model == config.arg_all:
        performUnderstandCFSScoreS()
        performUnderstandCFSScoreM()
        performUnderstandCFSScoreL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performUnderstandAll(type, model):
    if type == config.arg_type_vul:
        performUnderstandAllVul(model)
    elif type == config.arg_type_score:
        performUnderstandAllScore(model)
    elif type == config.arg_all:
        performUnderstandAllVul(model)
        performUnderstandAllScore(model)
    else:
        logging.error("Agrument Error - Please use vul, score or all as argument for type")

def performUnderstandCFS(type, model):
    if type == config.arg_type_vul:
        performUnderstandCFSVul(model)
    elif type == config.arg_type_score:
        performUnderstandCFSScore(model)
    elif type == config.arg_all:
        performUnderstandCFSVul(model)
        performUnderstandCFSScore(model)
    else:
        logging.error("Agrument Error - Please use vul, score or all as argument for type")

def performUnderstand(subset, type, model):
    if subset == config.arg_subset_all:
        performUnderstandAll(type, model)
    elif subset == config.arg_subset_cfs:
        performUnderstandCFS(type, model)
    elif subset == config.arg_subset_both:
        performUnderstandAll(type, model)
        performUnderstandCFS(type, model)
    else:
        logging.error("Argument Error - Please use cfs, both or all as argument for subset")
