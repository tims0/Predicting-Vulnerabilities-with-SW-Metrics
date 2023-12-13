import logging
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config
from models import models
from metric_extraction import extractFileMetricsFromRepo_analizo
from data_preprocessing import preprocessFileDataset_analizo
from correlation_analysis import correlationAnalysis_analizo
from feature_selection import featureSelection_analizo
from centralized_execution import centralized_analizo

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "analizo.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def extractFileMetricsFromRepoAnalizo():
    extractFileMetricsFromRepo_analizo.extractAnalizoMetricsFromRepo()

def preprocessFileDatasetAnalizo():
    preprocessFileDataset_analizo.preprocess_analizo_dataset()

def correlationAnalysisAnalizo():
    correlationAnalysis_analizo.perform_correalation_analysis_and_tests()

def featureSelectionAnalizo():
    featureSelection_analizo.perform_analizo_feature_selection()

def performAnalizoAllVulS():
    models.createAndSaveModelS(config.analizo_all_models["input"], config.analizo_all_models["S_Path"])
    centralized_analizo.performAnalizoAllVul(config.analizo_all_models["S_Path"], config.analizo_all_s)

def performAnalizoAllVulM():
    models.createAndSaveModelM(config.analizo_all_models["input"], config.analizo_all_models["M_Path"])
    centralized_analizo.performAnalizoAllVul(config.analizo_all_models["M_Path"], config.analizo_all_m)

def performAnalizoAllVulL():
    models.createAndSaveModelL(config.analizo_all_models["input"], config.analizo_all_models["L_Path"])
    centralized_analizo.performAnalizoAllVul(config.analizo_all_models["L_Path"], config.analizo_all_l)

def performAnalizoAllScoreS():
    models.createAndSaveModelS(config.analizo_all_models["input"], config.analizo_all_models["S_Path"])
    centralized_analizo.performAnalizoAllScore(config.analizo_all_models["S_Path"], config.analizo_all_s)

def performAnalizoAllScoreM():
    models.createAndSaveModelM(config.analizo_all_models["input"], config.analizo_all_models["M_Path"])
    centralized_analizo.performAnalizoAllScore(config.analizo_all_models["M_Path"], config.analizo_all_m)

def performAnalizoAllScoreL():
    models.createAndSaveModelL(config.analizo_all_models["input"], config.analizo_all_models["L_Path"])
    centralized_analizo.performAnalizoAllScore(config.analizo_all_models["L_Path"], config.analizo_all_l)

def performAnalizoCFSVulS():
    models.createAndSaveModelS(config.analizo_cfs_vul_models["input"], config.analizo_cfs_vul_models["S_Path"])
    centralized_analizo.performAnalizoCFSVul(config.analizo_all_models["S_Path", config.analizo_cfs_s])

def performAnalizoCFSVulM():
    models.createAndSaveModelM(config.analizo_cfs_vul_models["input"], config.analizo_cfs_vul_models["M_Path"])
    centralized_analizo.performAnalizoCFSVul(config.analizo_all_models["M_Path"], config.analizo_cfs_m)

def performAnalizoCFSVulL():
    models.createAndSaveModelL(config.analizo_cfs_vul_models["input"], config.analizo_cfs_vul_models["L_Path"])
    centralized_analizo.performAnalizoCFSVul(config.analizo_all_models["L_Path"], config.analizo_cfs_l)

def performAnalizoCFSScoreS():
    models.createAndSaveModelS(config.analizo_cfs_score_models["input"], config.analizo_cfs_score_models["S_Path"])
    centralized_analizo.performAnalizoCFSScore(config.analizo_all_models["S_Path"], config.analizo_cfs_s)

def performAnalizoCFSScoreM():
    models.createAndSaveModelM(config.analizo_cfs_score_models["input"], config.analizo_cfs_score_models["M_Path"])
    centralized_analizo.performAnalizoCFSScore(config.analizo_all_models["M_Path"], config.analizo_all_m)

def performAnalizoCFSScoreL():
    models.createAndSaveModelL(config.analizo_cfs_score_models["input"], config.analizo_cfs_score_models["L_Path"])
    centralized_analizo.performAnalizoCFSScore(config.analizo_all_models["L_Path"], config.analizo_cfs_l)

def performAnalizoAllVul(model):
    if model == config.arg_model_l:
        performAnalizoAllVulL()
    elif model == config.arg_model_m:
        performAnalizoAllVulM()
    elif model == config.arg_model_s:
        performAnalizoAllVulS()
    elif model == config.arg_all:
        performAnalizoAllVulS()
        performAnalizoAllVulM()
        performAnalizoAllVulL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performAnalizoAllScore(model):
    if model == config.arg_model_l:
        performAnalizoAllScoreL()
    elif model == config.arg_model_m:
        performAnalizoAllScoreM()
    elif model == config.arg_model_s:
        performAnalizoAllScoreS()
    elif model == config.arg_all:
        performAnalizoAllScoreS()
        performAnalizoAllScoreM()
        performAnalizoAllScoreL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performAnalizoCFSVul(model):
    if model == config.arg_model_l:
        performAnalizoCFSVulL()
    elif model == config.arg_model_m:
        performAnalizoCFSVulM()
    elif model == config.arg_model_s:
        performAnalizoCFSVulS()
    elif model == config.arg_all:
        performAnalizoCFSVulS()
        performAnalizoCFSVulM()
        performAnalizoCFSVulL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performAnalizoCFSScore(model):
    if model == config.arg_model_l:
        performAnalizoCFSScoreL()
    elif model == config.arg_model_m:
        performAnalizoCFSScoreM()
    elif model == config.arg_model_s:
        performAnalizoCFSScoreS()
    elif model == config.arg_all:
        performAnalizoCFSScoreS()
        performAnalizoCFSScoreM()
        performAnalizoCFSScoreL()
    else:
        logging.error("Argument Error - Please use L, M, S or all as argument for model")

def performAnalizoAll(type, model):
    if type == config.arg_type_vul:
        performAnalizoAllVul(model)
    elif type == config.arg_type_score:
        performAnalizoAllScore(model)
    elif type == config.arg_all:
        performAnalizoAllVul(model)
        performAnalizoAllScore(model)
    else:
        logging.error("Agrument Error - Please use vul, score or all as argument for type")

def performAnalizoCFS(type, model):
    if type == config.arg_type_vul:
        performAnalizoCFSVul(model)
    elif type == config.arg_type_score:
        performAnalizoCFSScore(model)
    elif type == config.arg_all:
        performAnalizoCFSVul(model)
        performAnalizoCFSScore(model)
    else:
        logging.error("Agrument Error - Please use vul, score or all as argument for type")

def performAnalizo(subset, type, model):
    if subset == config.arg_subset_all:
        performAnalizoAll(type, model)
    elif subset == config.arg_subset_cfs:
        performAnalizoCFS(type, model)
    elif subset == config.arg_subset_both:
        performAnalizoAll(type, model)
        performAnalizoCFS(type, model)
    else:
        logging.error("Argument Error - Please use cfs, both or all as argument for subset")
