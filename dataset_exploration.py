# Dataset CVEfixes last update on 03.07.2023
from config import config
import logging
import os
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "dataset_exploration.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def createDBConnection():
    return sqlite3.connect(config.db_file, timeout=10)

def createSummary(conn):
    # Getting numbers of CVEs in CVEfixes
    sql_cve = "SELECT COUNT(*) FROM cve"
    cursor_cve = conn.execute(sql_cve)
    cve = cursor_cve.fetchone()[0]

    # Getting numbers of CWEs in CWEfixes
    sql_cwe = "SELECT COUNT(*) FROM cwe"
    cursor_cwe = conn.execute(sql_cwe)
    cwe = cursor_cwe.fetchone()[0]

    # Getting numbers of projects in CWEfixes
    sql_repo = "SELECT COUNT(*) FROM repository"
    cursor_repo = conn.execute(sql_repo)
    repo = cursor_repo.fetchone()[0]

    # Getting numbers of commits in CWEfixes
    sql_commit = "SELECT COUNT(*) FROM commits"
    cursor_commit = conn.execute(sql_commit)
    commit = cursor_commit.fetchone()[0]

    # Getting numbers of files in CWEfixes
    sql_file = "SELECT COUNT(*) FROM file_change"
    cursor_file = conn.execute(sql_file)
    file = cursor_file.fetchone()[0]

    # Getting numbers of methods in CWEfixes
    sql_method = "SELECT COUNT(*) FROM method_change"
    cursor_method = conn.execute(sql_method)
    method = cursor_method.fetchone()[0]

    return pd.DataFrame([[cve,cwe,repo,commit,file,method]],columns=['CVEs','CWEs','projects','commits','files','methods'])

def getTop10ProjectsCVE(conn):
    # Getting Top 10 projects with most CVE and their average scores
    sql_top_projects = '''SELECT repo_name, COUNT(DISTINCT cve.cve_id) as CVEs, AVG(cve.cvss2_base_score) as CVSS2, AVG(cve.cvss3_base_score) as CVSS3, AVG(cve.exploitability_score) as exploitability, AVG(cve.impact_score) as impact
                        FROM repository, commits, fixes, cve
                        WHERE repository.repo_url = commits.repo_url AND commits.repo_url = fixes.repo_url AND fixes.cve_id = cve.cve_id
                        GROUP BY repo_name
                        ORDER BY CVEs DESC
                        LIMIT 10'''
    return pd.read_sql(sql_top_projects, conn)

def getTop10ProjectsCommits(conn):
    # Getting Top 10 projects with most commits
    sql_top_commits = '''SELECT repo_name, COUNT(commits.hash) as "commits"
                        FROM repository, commits
                        WHERE repository.repo_url = commits.repo_url
                        GROUP BY repo_name
                        ORDER BY "commits" DESC
                        LIMIT 10'''
    return pd.read_sql(sql_top_commits, conn)
    # TODO: Output df_top10_commits as table file/figure or json

def getTop10ProjectsFiles(conn):
    # Getting Top 10 projects with most files
    sql_top_files = '''SELECT repo_name, COUNT(DISTINCT file_change.file_change_id) as files
                    FROM repository, commits, file_change
                    WHERE repository.repo_url = commits.repo_url AND commits.hash = file_change.hash
                    GROUP BY repo_name
                    ORDER BY files DESC
                    LIMIT 10'''
    return pd.read_sql(sql_top_files, conn)

def getTop10ProjectsMethods(conn):
    # Getting Top 10 projects with most methods
    sql_top_methods = '''SELECT repo_name, COUNT(DISTINCT method_change.method_change_id) as methods
                        FROM repository, commits, file_change, method_change
                        WHERE repository.repo_url = commits.repo_url AND commits.hash = file_change.hash AND file_change.file_change_id = method_change.file_change_id
                        GROUP BY repo_name
                        ORDER BY methods DESC
                        LIMIT 10'''
    return pd.read_sql(sql_top_methods, conn)

def getTop10CWE(conn):
    # Getting Top 10 CWEs with most CVEs
    sql_top_cwe = '''SELECT cwe.cwe_id, cwe.cwe_name, COUNT(DISTINCT cve.cve_id) as CVEs, COUNT(DISTINCT commits.hash) as cmts, COUNT(DISTINCT file_change.file_change_id) as files
                    FROM cwe, cwe_classification, cve, fixes, commits, file_change
                    WHERE cwe.cwe_id = cwe_classification.cwe_id AND cwe_classification.cve_id = cve.cve_id AND cve.cve_id = fixes.cve_id AND fixes.hash = commits.hash AND commits.hash = file_change.hash
                    GROUP BY cwe.cwe_id
                    ORDER BY CVEs DESC
                    LIMIT 10'''
    return pd.read_sql(sql_top_cwe, conn)
    # TODO: Output df_top10_cwe as table file/figure or json

def getViolinPlotCVSS(conn):
    # Getting violin plot for CVSS base scores and average exploitability and impact on average for every project
    sql_cve_violin = '''SELECT repo_name, COUNT(DISTINCT cve.cve_id) as CVEs, AVG(cve.cvss2_base_score) as CVSS2, AVG(cve.cvss3_base_score) as CVSS3, AVG(cve.exploitability_score) as exploitability, AVG(cve.impact_score) as impact
                        FROM repository, commits, fixes, cve
                        WHERE repository.repo_url = commits.repo_url AND commits.repo_url = fixes.repo_url AND fixes.cve_id = cve.cve_id
                        GROUP BY repo_name
                        ORDER BY CVEs DESC'''
    df_cve_violoin = pd.read_sql(sql_cve_violin, conn)

    fig, axes = plt.subplots()

    axes.violinplot(dataset = [df_cve_violoin["impact"].values,
                            df_cve_violoin["exploitability"].values,
                            df_cve_violoin["CVSS3"].values,
                            df_cve_violoin["CVSS2"].values], vert=False)

    axes.yaxis.grid(True)
    axes.set_xlabel('Metric score')
    axes.set_yticks([1,2,3,4])
    axes.set_yticklabels(['avg impact', 'avg exploitability', 'avg CVSS3 base', 'avg CVSS2 base'])
    axes.set_ylabel('Vulnerability severity measures')

    plt.savefig(config.dataset_exploration_files["violin_plot_cvss"])
    plt.clf()

def getViolinPlotDMM(conn):
    # Getting violin plot for unit sizes, complexities, interfaces and for DMM scores on average for every project
    sql_dmm_violin = '''SELECT repository.repo_name, AVG(commits.dmm_unit_complexity) as complexity, AVG(commits.dmm_unit_interfacing) as interface, AVG(commits.dmm_unit_size) as unit_size, (AVG(commits.dmm_unit_complexity + commits.dmm_unit_interfacing + commits.dmm_unit_size) / 3) as dmm
                        FROM repository, commits
                        WHERE repository.repo_url = commits.repo_url
                        GROUP BY repository.repo_name'''
    df_dmm_violoin = pd.read_sql(sql_dmm_violin, conn)

    fig, axes = plt.subplots()

    axes.violinplot(dataset = [df_dmm_violoin["dmm"].values,
                            df_dmm_violoin["interface"].values,
                            df_dmm_violoin["complexity"].values,
                            df_dmm_violoin["unit_size"].values],
                            vert=False)

    axes.yaxis.grid(True)
    axes.set_xlabel('Metric score')
    axes.set_yticks([1,2,3,4])
    axes.set_yticklabels(['avg DMM score', 'avg unit interfacing', 'avg unit complexity', 'avg unit size'])
    axes.set_ylabel('Delta maintainability index')

    plt.savefig(config.dataset_exploration_files["violin_plot_dmm"])
    plt.clf()

def storeDataFrameToJSON(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_json(filename, orient="records", indent=4)

def performDatasetExploration():
    conn = createDBConnection()
    
    df_summary = createSummary(conn)
    storeDataFrameToJSON(df_summary, config.dataset_exploration_files["summary"])

    df_top10_projects_cve = getTop10ProjectsCVE(conn)
    storeDataFrameToJSON(df_top10_projects_cve, config.dataset_exploration_files["top10_projects_cve"])

    df_top10_projects_commits = getTop10ProjectsCommits(conn)
    storeDataFrameToJSON(df_top10_projects_commits, config.dataset_exploration_files["top10_commits"])

    df_top10_projects_files = getTop10ProjectsFiles(conn)
    storeDataFrameToJSON(df_top10_projects_files, config.dataset_exploration_files["top10_files"])

    df_top10_projects_methods = getTop10ProjectsMethods(conn)
    storeDataFrameToJSON(df_top10_projects_methods, config.dataset_exploration_files["top10_methods"])

    df_top10_cwe = getTop10CWE(conn)
    storeDataFrameToJSON(df_top10_cwe, config.dataset_exploration_files["top10_cwe"])

    getViolinPlotCVSS(conn)
    getViolinPlotDMM(conn)
