# libraries
import logging
import matplotlib.pyplot as plt
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from scipy.stats import ks_2samp # used for k-s-test
from scipy.stats import ttest_ind # used for t-test
import seaborn as sns # used for correlation heatmaps
from sklearn.impute import SimpleImputer # used for handling missing data
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config

sns.set(rc={'figure.figsize':(125,125)})
os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "correlationAnalysis.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

# Preparing dataset for correlation analysis
def prepare_correlation_analysis(df_corr):
    logging.info("Preparation of correlation analysis..")
    df_corr = df_corr.drop(columns=[config.column_repo_url])
    df_corr_columns = df_corr.columns
    imputer_corr = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0)
    imputer_corr = imputer_corr.fit(df_corr)
    df_corr = pd.DataFrame(imputer_corr.transform(df_corr), columns=df_corr_columns)
    df_corr = df_corr.astype(float)
    logging.info("Preparation of correlation analysis finished.")

    return df_corr

def correlation_analysis(df_corr, method):
    corr_pearson = df_corr.corr(method=method)
    return sns.heatmap(corr_pearson, vmin=-1, vmax=1, annot=True, cmap="rocket_r")

def save_heatmap_as_svg(heatmap, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fig_heatmap = heatmap.get_figure()
    fig_heatmap.savefig(filename)

def correlation_analysis_and_save(df_corr, method, filename):
    fig_heatmap = correlation_analysis(df_corr, method)
    save_heatmap_as_svg(fig_heatmap, filename)
    plt.clf()

def perform_all_correlation_analysis(df_corr, filename):
    prepare_correlation_analysis(df_corr)
    logging.info("Execution of pearson correlation analysis..")
    correlation_analysis_and_save(df_corr, 'pearson', filename["pearson"])
    logging.info("Pearson correlation analysis finished.")
    logging.info("Execution of spearman correlation analysis..")
    correlation_analysis_and_save(df_corr, 'spearman', filename["spearman"])
    logging.info("Spearman correlation analysis finished.")
    logging.info("Execution of kendall correlation analysis..")
    correlation_analysis_and_save(df_corr, 'kendall', filename["kendall"])
    logging.info("Kendall correlation analysis finished.")

def t_test(df_corr, test_column, threshold):
    list = []

    # iterating through all columns of df_corr
    for column in df_corr:

        # special case: skip observation of test_column
        if column == test_column:
            continue

        stat_vul_t, pvalue_vul_t = ttest_ind(df_corr[column], df_corr[test_column], equal_var=False)
        if pvalue_vul_t > threshold:
            decision_vul_t = "Accepted"
        else:
            decision_vul_t = "Rejected"
        list.append([column, stat_vul_t, pvalue_vul_t, decision_vul_t])

    return pd.DataFrame.from_records(list, columns=['Column', 'Statistics', 'p-Value', 'T-Test'])

def ks_test(df_corr, test_column, threshold):
    list = []

    # iterating through all columns of df_corr
    for column in df_corr:

        # special case: skip observation of test_column
        if column == test_column:
            continue

        stat_vul_t, pvalue_vul_t = ks_2samp(df_corr[column], df_corr[test_column])
        if pvalue_vul_t > threshold:
            decision_vul_t = "Accepted"
        else:
            decision_vul_t = "Rejected"
        list.append([column, stat_vul_t, pvalue_vul_t, decision_vul_t])
    
    return pd.DataFrame.from_records(list, columns=['Column', 'Statistics', 'p-Value', 'KS-Test'])

def store_test_results_to_json(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_json(filename, orient="records", indent=4)

def perform_all_tests(df_corr, threshold, filename):
    logging.info("Execution of significance tests..")
    df_corr = prepare_correlation_analysis(df_corr)
    t_test_vul = t_test(df_corr, config.column_vul, threshold)
    t_test_score = t_test(df_corr, config.column_score, threshold)
    ks_test_vul = ks_test(df_corr, config.column_vul, threshold)
    ks_test_score = ks_test(df_corr, config.column_score, threshold)

    store_test_results_to_json(t_test_vul, filename['t_test_vul'])
    store_test_results_to_json(t_test_score, filename['t_test_score'])
    store_test_results_to_json(ks_test_vul, filename['ks_test_vul'])
    store_test_results_to_json(ks_test_score, filename['ks_test_score'])
    logging.info("Significance tests finished.")
