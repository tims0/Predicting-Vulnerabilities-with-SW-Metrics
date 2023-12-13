# libraries
import os
import sys
import logging
from math import sqrt
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from scipy.stats import pointbiserialr
from sklearn.impute import SimpleImputer
# CFS: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=0e78b20b27d27261f9ae088eb13201f2d5b185bd

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "featureSelection.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def prepare_feature_selection(dataset):
    # Preparing dataset for feature selection
    logging.info("Preparing dataset for feature selection..")
    dataset = dataset.drop(columns=[config.column_repo_url])
    dataset_columns = dataset.columns
    imputer_corr = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0)
    imputer_corr = imputer_corr.fit(dataset)
    dataset = pd.DataFrame(imputer_corr.transform(dataset), columns=dataset_columns)
    dataset = dataset.astype(float)
    logging.info("Dataset preparation finished")

    return dataset

# Implementation of the evaluation function merit with dataframe, subset and label names as inputs for calculation of average feature-class correlation
def getMerit(df, subset, label):
    k = len(subset)

    # average feature-class correlation
    rcf_all = []
    for feature in subset:
        coeff = pointbiserialr( df[label], df[feature] )
        rcf_all.append( abs( coeff.correlation ) )
    rcf = np.mean( rcf_all )

    # average feature-feature correlation
    corr = df[subset].corr()
    corr.values[np.tril_indices_from(corr.values)] = np.nan
    corr = abs(corr)
    rff = corr.unstack().mean()

    return (k * rcf) / sqrt(k + k * (k-1) * rff)

# Implementation of priority queue with feature subsets as items and corresponding metrics as priority for returning the items with highest priority
class PriorityQueue:
    def  __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
    
    def push(self, item, priority):
        """
        item already in priority queue with smaller priority:
        -> update its priority
        item already in priority queue with higher priority:
        -> do nothing
        if item not in priority queue:
        -> push it
        """
        for index, (i, p) in enumerate(self.queue):
            if (set(i) == set(item)):
                if (p >= priority):
                    break
                del self.queue[index]
                self.queue.append( (item, priority) )
                break
        else:
            self.queue.append( (item, priority) )
        
    def pop(self):
        # return item with highest priority and remove it from queue
        max_idx = 0
        for index, (i, p) in enumerate(self.queue):
            if (self.queue[max_idx][1] < p):
                max_idx = index
        (item, priority) = self.queue[max_idx]
        del self.queue[max_idx]
        return (item, priority)

def getFirstFeature(dataset, features, label):
    best_value = -1
    best_feature = ''

    for feature in features:
        coeff = pointbiserialr( dataset[label], dataset[feature] )
        abs_coeff = abs ( coeff.correlation )
        if abs_coeff > best_value:
            best_value = abs_coeff
            best_feature = feature
    logging.info("Feature %s with highest merit %.4f as first element of correlation based feature selection"%(best_feature, best_value))

    return best_feature, best_value

def performFeatureSelection(dataset, label, max_backtrack):
    # Getting list of features
    logging.info("Preparing correlation based feature selection..")
    features = dataset.columns.tolist()
    features.remove(config.column_vul)
    features.remove(config.column_score)

    # Compute feature with highest correlation
    best_feature, best_value = getFirstFeature(dataset, features, label)

    # Initialize queue
    queue = PriorityQueue()

    # Push first tuple (subset, merit)
    queue.push([best_feature], best_value)

    # list for visited nodes
    visited = []
    visited.append([best_feature])

    # counter for backtracks
    n_backtrack = 0
    logging.info("Preparations for correlation based feature selection finished.")

    # Repeat until queue is empty or the maximum number of backtracks is reached
    logging.info("Calculating further features for correlation based feature selection")
    while not queue.isEmpty():
        # Get element of queue with highest merit
        subset, priority = queue.pop()
        
        # Check whether the priority of this subset is higher than the current best subset
        if (priority < best_value):
            n_backtrack += 1
        else:
            best_value = priority
            best_subset = subset

        # Goal condition
        if (n_backtrack == max_backtrack):
            break
        
        # iterate through all features and look of one can increase the merit
        for feature in features:
            temp_subset = subset + [feature]
            
            # check if this subset has already been evaluated
            for node in visited:
                if (set(node) == set(temp_subset)):
                    break
            # if not, ...
            else:
                # ... mark it as visited
                visited.append( temp_subset )
                # ... compute merit
                merit = getMerit(dataset, temp_subset, label)
                # and push it to the queue
                queue.push(temp_subset, merit)

    logging.info("Calculation of further features for correlation based feature selection finished.")
    return best_subset, best_value

def createSelectedDataset(dataset, subset, label):
    logging.info("Generating cfs dataset..")
    subset.append(config.column_repo_url)
    subset.append(label)
    dataset = dataset[subset]
    logging.info("CFS datadest generated.")

    return dataset