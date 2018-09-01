import numpy as np
import pandas as pd
from keras import layers, models
from keras import regularizers
from keras import optimizers
from sklearn.model_selection import train_test_split
from keras import callbacks
# preprocessing
from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.utils import np_utils

from . import word_vectors
from .. import settings

def get_word2vec_nn( input_shape , num_classes):
    model = models.Sequential()
    model.add( layers.convolutional.Conv1D( filters=500, kernel_size=3, padding='same', activation='relu',
        input_shape=input_shape))
    model.add( layers.convolutional.MaxPooling1D( pool_size=2))
    model.add( layers.Dropout(0.2))
    model.add( layers.Bidirectional( layers.LSTM(100, dropout=0.2) ) )
    model.add( layers.Dense(num_classes, activation='softmax',
    kernel_regularizer=regularizers.l2(0.01),activity_regularizer=regularizers.l1(0.01)))
    optimizer = optimizers.RMSprop()
    model.compile( loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    print( model.summary() )
    return model

def start_training():
    TOP_WORDS = 200000
    MAX_SENTENCE_LENGTH = 56
    EMBEDDING_VECTOR_LENGTH = 300
    NUM_CLASSES = 3
    EPOCHS = 100
    SEQUENCE_LENGTH = 65
    EMBEDDING_DIM = 300
    INPUT_SHAPE = ( SEQUENCE_LENGTH, EMBEDDING_DIM )
    WORD2VEC_MODEL = word_vectors.load_word2vec_model( settings.WORD2VEC_PATH, is_binary=True )
    WEIGHTS_TARGET_PATH = settings.NN_BASE_WEIGHTS
    model = get_word2vec_nn( INPUT_SHAPE , NUM_CLASSES)
    model.load_weights( WEIGHTS_TARGET_PATH )
    print("Done!")
