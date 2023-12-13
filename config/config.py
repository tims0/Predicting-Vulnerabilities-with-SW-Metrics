import logging
import os

### General configuration variables
path = os.path.dirname(os.path.dirname(__file__))
db_file = path + "/CVEfixes-main/Data/CVEfixes.db"
output_path = path + "/output/"
repo_path = path + "metric_extraction/repo/"

log_path = path + "/log/"
log_format = "%(asctime)s - %(levelname)s:%(message)s"
log_level = logging.INFO
log_datefmt = "%Y-%m-%d %H:%M:%S"

file_id_sql_col = "file_change_id"
column_repo_url = 'remainder__repo_url'
column_vul = "remainder__before_change"
column_score = "remainder__cvss3_base_score"

correlation_threshold = 0.05
max_backtrack = 5
epoch = 20

# Main
bash_cvefixes_from_scratch = './CVEfixes-main/Coed/create_CVEfixes_from_scratch.sh'
arg_understand = "understand"
arg_analizo = "analizo"
arg_combined = "combined"
arg_all = "all"
arg_model_l = "L"
arg_model_m = "M"
arg_model_s = "S"
arg_subset_all = "all"
arg_subset_cfs = "cfs"
arg_subset_both = "both"
arg_type_vul = "vul"
arg_type_score = "score"
arg_command_updateDatabase = "updateDatabase"
arg_command_extractMetrics = "extractMetrics"
arg_command_preprocessDataset = "preprocessDataset"
arg_command_correlationAnalysis = "correlationAnalysis"
arg_command_featureSelection = "featureSelection"
arg_command_performModelExecution = "performModelExecution"

# Dataset exploration
dataset_exploration_files = {
    "summary": output_path + "dataset_exploration/dataset_summary.json",
    "top10_projects_cve": output_path + "dataset_exploration/dataset_top10_projects_cve.json",
    "top10_commits": output_path + "dataset_exploration/dataset_top10_commits.json",
    "top10_files": output_path + "dataset_exploration/dataset_top10_files.json",
    "top10_methods": output_path + "dataset_exploration/dataset_top10_methods.json",
    "top10_cwe": output_path + "dataset_exploration/dataset_top10_cwe.json",
    "violin_plot_cvss": output_path + "dataset_exploration/violin_plot_cvss.svg",
    "violin_plot_dmm": output_path + "dataset_exploration/violin_plot_dmm.svg"
}

# Understand specific
understand_metrics_table = "file_metrics_understand"
udb_file = repo_path + "/project.und"
csv_file = repo_path + "/project.csv"
understand_dataset_all = output_path + "understand_file_dataset_with_all_informations.json"
understand_dataset_necessary = output_path + "understand_file_dataset_necessary_informations.json"
understand_dataset_cfs_vul = output_path + "understand_file_dataset_cfs_vul.json"
understand_dataset_cfs_score = output_path + "understand_file_dataset_cfs_score.json"
understand_correlation_files = {
    "pearson": output_path + "understand/ht_pearson.svg",
    "spearman": output_path + "understand/ht_spearman.svg",
    "kendall": output_path + "understand/ht_kendall.svg",
    "t_test_vul": output_path + "understand/t_test_vul.json",
    "t_test_score": output_path + "understand/t_test_score.json",
    "ks_test_vul": output_path + "understand/ks_test_vul.json",
    "ks_test_score": output_path + "understand/ks_test_score.json"
}
understand_csv_files = {
    "x_train": output_path + '/understand_all/x_train.csv',
    "y_train": output_path + '/understand_all/y_train.csv',
    "x_test": output_path + '/understand_all/x_test.csv',
    "y_test": output_path + '/understand_all/y_test.csv',
    "x_val": output_path + '/understand_all/x_val.csv',
    "y_val": output_path + '/understand_all/y_val.csv'
}
understand_cfs_vul_files = {
    "x_train": output_path + '/understand_cfs_vul/x_train.csv',
    "y_train": output_path + '/understand_cfs_vul/y_train.csv',
    "x_test": output_path + '/understand_cfs_vul/x_test.csv',
    "y_test": output_path + '/understand_cfs_vul/y_test.csv',
    "x_val": output_path + '/understand_cfs_vul/x_val.csv',
    "y_val": output_path + '/understand_cfs_vul/y_val.csv'
}
understand_cfs_score_files = {
    "x_train": output_path + '/understand_cfs_score/x_train.csv',
    "y_train": output_path + '/understand_cfs_score/y_train.csv',
    "x_test": output_path + '/understand_cfs_score/x_test.csv',
    "y_test": output_path + '/understand_cfs_score/y_test.csv',
    "x_val": output_path + '/understand_cfs_score/x_val.csv',
    "y_val": output_path + '/understand_cfs_score/y_val.csv'
}
understand_all_models = {
    "input": 107,
    "S_Path": output_path + "/understand_all/Model_S.h5",
    "M_Path": output_path + "/understand_all/Model_M.h5",
    "L_Path": output_path + "/understand_all/Model_L.h5"
}
understand_cfs_vul_models = {
    "input": 1,
    "S_Path": output_path + "/understand_cfs_vul/Model_S.h5",
    "M_Path": output_path + "/understand_cfs_vul/Model_M.h5",
    "L_Path": output_path + "/understand_cfs_vul/Model_L.h5"
}
understand_cfs_score_models = {
    "input": 2,
    "S_Path": output_path + "/understand_cfs_score/Model_S.h5",
    "M_Path": output_path + "/understand_cfs_score/Model_M.h5",
    "L_Path": output_path + "/understand_cfs_score/Model_L.h5"
}
understand_all_s = {
    "score_plot_accuracy": output_path + "/understand_all/score_plot_accuracy_S.svg",
    "score_plot_loss": output_path + "/understand_all/score_plot_loss_S.svg",
    "score_submission": output_path + "/understand_all/score_submission_S.csv",
    "vul_plot": output_path + "/understand_all/vul_plot_S.csv"
}
understand_all_m = {
    "score_plot_accuracy": output_path + "/understand_all/score_plot_accuracy_M.svg",
    "score_plot_loss": output_path + "/understand_all/score_plot_loss_M.svg",
    "score_submission": output_path + "/understand_all/score_submission_M.csv",
    "vul_plot": output_path + "/understand_all/vul_plot_M.csv"
}
understand_all_l = {
    "score_plot_accuracy": output_path + "/understand_all/score_plot_accuracy_L.svg",
    "score_plot_loss": output_path + "/understand_all/score_plot_loss_L.svg",
    "score_submission": output_path + "/understand_all/score_submission_L.csv",
    "vul_plot": output_path + "/understand_all/vul_plot_L.csv"
}
understand_cfs_s = {
    "score_plot_accuracy": output_path + "/understand_cfs_score/score_plot_accuracy_S.svg",
    "score_plot_loss": output_path + "/understand_cfs_score/score_plot_loss_S.svg",
    "score_submission": output_path + "/understand_cfs_score/score_submission_S.csv",
    "vul_plot": output_path + "/understand_cfs_vul/vul_plot_S.csv"
}
understand_cfs_m = {
    "score_plot_accuracy": output_path + "/understand_cfs_score/score_plot_accuracy_M.svg",
    "score_plot_loss": output_path + "/understand_cfs_score/score_plot_loss_M.svg",
    "score_submission": output_path + "/understand_cfs_score/score_submission_M.csv",
    "vul_plot": output_path + "/understand_cfs_vul/vul_plot_M.csv"
}
understand_cfs_l = {
    "score_plot_accuracy": output_path + "/understand_cfs_score/score_plot_accuracy_L.svg",
    "score_plot_loss": output_path + "/understand_cfs_score/score_plot_loss_L.svg",
    "score_submission": output_path + "/understand_cfs_score/score_submission_L.csv",
    "vul_plot": output_path + "/understand_cfs_vul/vul_plot_L.csv"
}

# Analizo specific
analizo_metrics_table = "file_metrics_analizo"
yaml_file = repo_path + "/metrics.yaml"
analizo_dataset_all = output_path + "analizo_file_dataset_with_all_informations.json"
analizo_dataset_necessary = output_path + "analizo_file_dataset_necessary_informations.json"
analizo_dataset_cfs_vul = output_path + "analizo_file_dataset_cfs_vul.json"
analizo_dataset_cfs_score = output_path + "analizo_file_dataset_cfs_score.json"
analizo_correlation_files = {
    "pearson": output_path + "analizo/ht_pearson.svg",
    "spearman": output_path + "analizo/ht_spearman.svg",
    "kendall": output_path + "analizo/ht_kendall.svg",
    "t_test_vul": output_path + "analizo/t_test_vul.json",
    "t_test_score": output_path + "analizo/t_test_score.json",
    "ks_test_vul": output_path + "analizo/ks_test_vul.json",
    "ks_test_score": output_path + "analizo/ks_test_score.json"
}
analizo_csv_files = {
    "x_train": output_path + '/analizo_all/x_train.csv',
    "y_train": output_path + '/analizo_all/y_train.csv',
    "x_test": output_path + '/analizo_all/x_test.csv',
    "y_test": output_path + '/analizo_all/y_test.csv',
    "x_val": output_path + '/analizo_all/x_val.csv',
    "y_val": output_path + '/analizo_all/y_val.csv'
}
analizo_cfs_vul_files = {
    "x_train": output_path + '/analizo_cfs_vul/x_train.csv',
    "y_train": output_path + '/analizo_cfs_vul/y_train.csv',
    "x_test": output_path + '/analizo_cfs_vul/x_test.csv',
    "y_test": output_path + '/analizo_cfs_vul/y_test.csv',
    "x_val": output_path + '/analizo_cfs_vul/x_val.csv',
    "y_val": output_path + '/analizo_cfs_vul/y_val.csv'
}
analizo_cfs_score_files = {
    "x_train": output_path + '/analizo_cfs_score/x_train.csv',
    "y_train": output_path + '/analizo_cfs_score/y_train.csv',
    "x_test": output_path + '/analizo_cfs_score/x_test.csv',
    "y_test": output_path + '/analizo_cfs_score/y_test.csv',
    "x_val": output_path + '/analizo_cfs_score/x_val.csv',
    "y_val": output_path + '/analizo_cfs_score/y_val.csv'
}
analizo_all_models = {
    "input": 40,
    "S_Path": output_path + "/analizo_all/Model_S.h5",
    "M_Path": output_path + "/analizo_all/Model_M.h5",
    "L_Path": output_path + "/analizo_all/Model_L.h5"
}
analizo_cfs_vul_models = {
    "input": 1,
    "S_Path": output_path + "/analizo_cfs_vul/Model_S.h5",
    "M_Path": output_path + "/analizo_cfs_vul/Model_M.h5",
    "L_Path": output_path + "/analizo_cfs_vul/Model_L.h5"
}
analizo_cfs_score_models = {
    "input": 1,
    "S_Path": output_path + "/analizo_cfs_score/Model_S.h5",
    "M_Path": output_path + "/analizo_cfs_score/Model_M.h5",
    "L_Path": output_path + "/analizo_cfs_score/Model_L.h5"
}
analizo_all_s = {
    "score_plot_accuracy": output_path + "/analizo_all/score_plot_accuracy_S.svg",
    "score_plot_loss": output_path + "/analizo_all/score_plot_loss_S.svg",
    "score_submission": output_path + "/analizo_all/score_submission_S.csv",
    "vul_plot": output_path + "/analizo_all/vul_plot_S.csv"
}
analizo_all_m = {
    "score_plot_accuracy": output_path + "/analizo_all/score_plot_accuracy_M.svg",
    "score_plot_loss": output_path + "/analizo_all/score_plot_loss_M.svg",
    "score_submission": output_path + "/analizo_all/score_submission_M.csv",
    "vul_plot": output_path + "/analizo_all/vul_plot_M.csv"
}
analizo_all_l = {
    "score_plot_accuracy": output_path + "/analizo_all/score_plot_accuracy_L.svg",
    "score_plot_loss": output_path + "/analizo_all/score_plot_loss_L.svg",
    "score_submission": output_path + "/analizo_all/score_submission_L.csv",
    "vul_plot": output_path + "/analizo_all/vul_plot_L.csv"
}
analizo_cfs_s = {
    "score_plot_accuracy": output_path + "/analizo_cfs_score/score_plot_accuracy_S.svg",
    "score_plot_loss": output_path + "/analizo_cfs_score/score_plot_loss_S.svg",
    "score_submission": output_path + "/analizo_cfs_score/score_submission_S.csv",
    "vul_plot": output_path + "/analizo_cfs_vul/vul_plot_S.csv"
}
analizo_cfs_m = {
    "score_plot_accuracy": output_path + "/analizo_cfs_score/score_plot_accuracy_M.svg",
    "score_plot_loss": output_path + "/analizo_cfs_score/score_plot_loss_M.svg",
    "score_submission": output_path + "/analizo_cfs_score/score_submission_M.csv",
    "vul_plot": output_path + "/analizo_cfs_vul/vul_plot_M.csv"
}
analizo_cfs_l = {
    "score_plot_accuracy": output_path + "/analizo_cfs_score/score_plot_accuracy_L.svg",
    "score_plot_loss": output_path + "/analizo_cfs_score/score_plot_loss_L.svg",
    "score_submission": output_path + "/analizo_cfs_score/score_submission_L.csv",
    "vul_plot": output_path + "/analizo_cfs_vul/vul_plot_L.csv"
}

# Combined specific
combined_dataset_all = output_path + "combined_file_dataset_with_all_informations.json"
combined_dataset_necessary = output_path + "combined_file_dataset_necessary_informations.json"
combined_dataset_cfs_vul = output_path + "combined_file_dataset_cfs_vul.json"
combined_dataset_cfs_score = output_path + "combined_file_dataset_cfs_score.json"
combined_correlation_files = {
    "pearson": output_path + "combined/ht_pearson.svg",
    "spearman": output_path + "combined/ht_spearman.svg",
    "kendall": output_path + "combined/ht_kendall.svg",
    "t_test_vul": output_path + "combined/t_test_vul.json",
    "t_test_score": output_path + "combined/t_test_score.json",
    "ks_test_vul": output_path + "combined/ks_test_vul.json",
    "ks_test_score": output_path + "combined/ks_test_score.json"
}
combined_csv_files = {
    "x_train": output_path + '/combined_all/x_train.csv',
    "y_train": output_path + '/combined_all/y_train.csv',
    "x_test": output_path + '/combined_all/x_test.csv',
    "y_test": output_path + '/combined_all/y_test.csv',
    "x_val": output_path + '/combined_all/x_val.csv',
    "y_val": output_path + '/combined_all/y_val.csv'
}
combined_cfs_vul_files = {
    "x_train": output_path + '/combined_cfs_vul/x_train.csv',
    "y_train": output_path + '/combined_cfs_vul/y_train.csv',
    "x_test": output_path + '/combined_cfs_vul/x_test.csv',
    "y_test": output_path + '/combined_cfs_vul/y_test.csv',
    "x_val": output_path + '/combined_cfs_vul/x_val.csv',
    "y_val": output_path + '/combined_cfs_vul/y_val.csv'
}
combined_cfs_score_files = {
    "x_train": output_path + '/combined_cfs_score/x_train.csv',
    "y_train": output_path + '/combined_cfs_score/y_train.csv',
    "x_test": output_path + '/combined_cfs_score/x_test.csv',
    "y_test": output_path + '/combined_cfs_score/y_test.csv',
    "x_val": output_path + '/combined_cfs_score/x_val.csv',
    "y_val": output_path + '/combined_cfs_score/y_val.csv'
}
combined_all_models = {
    "input": 119,
    "S_Path": output_path + "/combined_all/Model_S.h5",
    "M_Path": output_path + "/combined_all/Model_M.h5",
    "L_Path": output_path + "/combined_all/Model_L.h5"
}
combined_cfs_vul_models = {
    "input": 1,
    "S_Path": output_path + "/combined_cfs_vul/Model_S.h5",
    "M_Path": output_path + "/combined_cfs_vul/Model_M.h5",
    "L_Path": output_path + "/combined_cfs_vul/Model_L.h5"
}
combined_cfs_score_models = {
    "input": 2,
    "S_Path": output_path + "/combined_cfs_score/Model_S.h5",
    "M_Path": output_path + "/combined_cfs_score/Model_M.h5",
    "L_Path": output_path + "/combined_cfs_score/Model_L.h5"
}
combined_all_s = {
    "score_plot_accuracy": output_path + "/combined_all/score_plot_accuracy_S.svg",
    "score_plot_loss": output_path + "/combined_all/score_plot_loss_S.svg",
    "score_submission": output_path + "/combined_all/score_submission_S.csv",
    "vul_plot": output_path + "/combined_all/vul_plot_S.csv"
}
combined_all_m = {
    "score_plot_accuracy": output_path + "/combined_all/score_plot_accuracy_M.svg",
    "score_plot_loss": output_path + "/combined_all/score_plot_loss_M.svg",
    "score_submission": output_path + "/combined_all/score_submission_M.csv",
    "vul_plot": output_path + "/combined_all/vul_plot_M.csv"
}
combined_all_l = {
    "score_plot_accuracy": output_path + "/combined_all/score_plot_accuracy_L.svg",
    "score_plot_loss": output_path + "/combined_all/score_plot_loss_L.svg",
    "score_submission": output_path + "/combined_all/score_submission_L.csv",
    "vul_plot": output_path + "/combined_all/vul_plot_L.csv"
}
combined_cfs_s = {
    "score_plot_accuracy": output_path + "/combined_cfs_score/score_plot_accuracy_S.svg",
    "score_plot_loss": output_path + "/combined_cfs_score/score_plot_loss_S.svg",
    "score_submission": output_path + "/combined_cfs_score/score_submission_S.csv",
    "vul_plot": output_path + "/combined_cfs_vul/vul_plot_S.csv"
}
combined_cfs_m = {
    "score_plot_accuracy": output_path + "/combined_cfs_score/score_plot_accuracy_M.svg",
    "score_plot_loss": output_path + "/combined_cfs_score/score_plot_loss_M.svg",
    "score_submission": output_path + "/combined_cfs_score/score_submission_M.csv",
    "vul_plot": output_path + "/combined_cfs_vul/vul_plot_M.csv"
}
combined_cfs_l = {
    "score_plot_accuracy": output_path + "/combined_cfs_score/score_plot_accuracy_L.svg",
    "score_plot_loss": output_path + "/combined_cfs_score/score_plot_loss_L.svg",
    "score_submission": output_path + "/combined_cfs_score/score_submission_L.csv",
    "vul_plot": output_path + "/combined_cfs_vul/vul_plot_L.csv"
}
