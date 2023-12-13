import logging
import math
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.metrics import Metric
from keras.callbacks import EarlyStopping
from scikeras.wrappers import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, precision_score, recall_score, f1_score
from sklearn.metrics import mean_squared_error, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
from matplotlib import rcParams
import time
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "centralized.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def getAllData(file_dict):
    x_train = pd.read(file_dict["x_train"])
    y_train = pd.read(file_dict["y_train"])
    x_test = pd.read(file_dict["x_test"])
    y_test = pd.read(file_dict["y_test"])
    x_val = pd.read(file_dict["x_val"])
    y_val = pd.read(file_dict["y_val"])

    return x_train, y_train, x_test, y_test, x_val, y_val

def getVulModel(model_path):
    model = keras.models.load_model(model_path)

    model.compile(
                optimizer=tf.keras.optimizers.SGD(),
                loss=tf.keras.losses.BinaryCrossentropy(), 
                metrics=[tf.keras.metrics.BinaryAccuracy(),tf.keras.metrics.AUC(), tf.keras.metrics.Recall()]
                )
    
    return model

def getScoreModel(model_path):
    model = keras.models.load_model(model_path)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss=tf.keras.losses.MeanSquaredError(), 
        metrics=['accuracy']
        )    

    return model

def trainVulModel(model, x_train, y_train, x_val, y_val):
    zeitanfang = time.time()

    initial_history = model.fit(
        x_train, 
        y_train, 
        epochs=config.epoch, 
        validation_data = (x_val, y_val)
        )

    zeitende = time.time()
    res=zeitende-zeitanfang
    logging.info("Dauer Programmausführung: ", res)

    return initial_history

def getScoreEstimator(model, x_train, y_train):
    zeitanfang = time.time()

    estimator = KerasRegressor(build_fn=model, epochs=100, batch_size=10, verbose=0)
    kfold = KFold(n_splits=10)
    results = cross_val_score(estimator, x_train, y_train, cv=kfold)  

    zeitende = time.time()
    res=zeitende-zeitanfang

    print("Dauer Estimatorberechnung: ", res)
    print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))
    print("Min: %.2f, Max: %.2f " % (results.min(), results.max()))

    return estimator

def trainScoreModel(estimator, x_train, y_train, x_val, y_val):
    zeitanfang = time.time()

    early_stopping = EarlyStopping(monitor='loss', patience=1, verbose=1) 
    initial_history = estimator.fit(x_train, y_train, validation_split=0.1, 
                            epochs=100, batch_size=10, 
                            callbacks=[early_stopping], 
                            verbose=1).history_

    zeitende = time.time()
    res=zeitende-zeitanfang
    print("Dauer Programmausführung: ", res)

    return initial_history

def predictAndEvaluateVulModel(model, initial_history, filename, x_train, y_train, x_test, y_test, x_val, y_val):
    y_train_pred = model.predict(x_train) 
    y_val_pred = model.predict(x_val)
    y_test_pred = model.predict(x_test)

    train_err, train_acc, train_auc, train_recall  = model.evaluate(x_train, y_train, verbose=0)
    val_err, val_acc, val_auc, val_recall = model.evaluate(x_val, y_val, verbose=0)
    test_err, test_acc, test_auc, test_recall = model.evaluate(x_test, y_test, verbose=0)

    y_train_pred = (y_train_pred>0.5)
    y_val_pred = (y_val_pred>0.5)
    y_test_pred = (y_test_pred>0.5)

    logging.info('Training data:')  
    logging.info('Accuracy on training data: {} %'.format(train_acc))  
    logging.info('Error on training data: {}'.format(train_err)) 

    logging.info('Recall on training data: {}'.format(recall_score(y_train, y_train_pred)))
    logging.info('Precision on training data: {}'.format(precision_score(y_train, y_train_pred)))
    logging.info('F1-score on training data: {}'.format(f1_score(y_train, y_train_pred)))

    logging.info('Test data:')  
    logging.info('Accuracy on test data: {} %'.format(test_acc))   
    logging.info('Error on test data: {}'.format(test_err))  
    logging.info('AUC on test data: {}'.format(test_auc))  
    logging.info('Recall on test data: {}'.format(test_recall))
    logging.info('Precision on test data: {}'.format(precision_score(y_test, y_test_pred)))
    logging.info('F1-score on test data: {}'.format(f1_score(y_test, y_test_pred)))


    logging.info('Validation data:')  
    logging.info('Accuracy on validation data: {} %'.format(val_acc))   
    logging.info('Error on validation data: {}'.format(val_err))  

    logging.info('Recall on validation data: {}'.format(recall_score(y_val, y_val_pred)))
    logging.info('Precision on validation data: {}'.format(precision_score(y_val, y_val_pred)))
    logging.info('F1-score on validation data: {}'.format(f1_score(y_val, y_val_pred)))

    
    rcParams['figure.figsize'] = (18, 8)
    rcParams['axes.spines.top'] = False
    rcParams['axes.spines.right'] = False 

    plt.plot( 
        initial_history.history['loss'], 
        label='Loss',
        lw=3
    )
    plt.plot(
        initial_history.history['binary_accuracy'], 
        label='Binary accuracy', lw=3
    )

    plt.plot(
        initial_history.history['auc'], 
        label='AUC', lw=3
    )

    plt.plot(
        initial_history.history['recall'], 
        label='Recall', lw=3
    )

    plt.title('Evaluation metrics', size=20)
    plt.xlabel('Epoch', size=14)
    plt.legend(loc='lower left');

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename["vul_plot"])
    plt.clf()

def predictAndEvaluateScoreModel(estimator, initial_history, filename, x_train, y_train, x_test, y_test, x_val, y_val):
    # list all data in history
    print(initial_history.keys())
    # summarize history for accuracy
    plt.plot(initial_history['accuracy'])
    plt.plot(initial_history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename["score_plot_accuracy"])
    plt.clf()

    # summarize history for loss
    plt.plot(initial_history['loss'])
    plt.plot(initial_history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename["score_plot_loss"])
    plt.clf()

    rmse = math.sqrt(mean_squared_error(y_val.values, estimator.predict(x_val.values)))
    print(rmse)
    pred = estimator.predict(x_test)
    test_df = pd.DataFrame({'y_pred': pred})

    print(len(test_df))

    submission = test_df
    submission.sort_index(inplace=True)
    submission.loc[submission['y_pred'] < 0, 'y_pred'] = 0
    submission.loc[submission['y_pred'] > 10, 'y_pred'] = 10
    submission.to_csv(filename["score_submission"], index=False)