import logging
import tensorflow as tf
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from config import config

os.makedirs(os.path.dirname(config.log_path), exist_ok=True)
logging.basicConfig(
    filename=config.log_path + "models.log", 
    format=config.log_format ,
    level=config.log_level,
    datefmt=config.log_datefmt)

def createAndSaveModelS(input, filename):
    model = tf.keras.Sequential([
        

        tf.keras.layers.InputLayer(input_shape=(input,)),
    
        tf.keras.layers.Dense(10, activation='relu'),
        
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.save(filename)

def createAndSaveModelM(input, filename):
    model = tf.keras.Sequential([
        

        tf.keras.layers.InputLayer(input_shape=(input,)),

        tf.keras.layers.Dense(200, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(200, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(150, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(120, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(70, activation='relu'),
        
        #output layer
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.save(filename)

def createAndSaveModelL(input, filename):
    model = tf.keras.Sequential([
        
        tf.keras.layers.InputLayer(input_shape=(input,)),

        tf.keras.layers.Dense(500, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(450, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(400, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(350, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(300, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(250, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(200, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(150, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(120, activation='relu'),
        tf.keras.layers.LayerNormalization(),
        tf.keras.layers.Dropout(0.5),
        
        tf.keras.layers.Dense(70, activation='relu'),
        
        #output layer
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.save(filename)
