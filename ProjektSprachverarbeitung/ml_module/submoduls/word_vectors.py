import numpy as np
from keras.preprocessing.text import text_to_word_sequence
from gensim.models import Word2Vec
from  gensim.models import keyedvectors


def comment_to_word2vec( comment, word2vec_model ):
    seq_len = 65
    vec_dim = 300
    sentence_as_wordlist = text_to_word_sequence( comment )
    data_matrix = np.zeros( ( 1,seq_len, vec_dim  ) )
    sentence_as_wordlist = sentence_as_wordlist[:seq_len]
    for i, word in enumerate( sentence_as_wordlist ):
        if word in word2vec_model.wv.vocab:
            word_vector = word2vec_model.wv[word]
        else:
            word_vector = np.ones( vec_dim )
        data_matrix[0][i] = word_vector
    return data_matrix

def comments_to_word_to_vec( comments, word2vec_model,seq_len, vec_dim ):
    word_2_vec_comments = np.zeros( ( len(comments), seq_len, vec_dim ) )
    for i, comment in enumerate( comments ):
        word_2_vec_comments[i] = comment_to_word2vec( comment,word2vec_model )
    return word_2_vec_comments

def load_word2vec_model( path, is_binary=False ):
    print( "Loading word2vec model..." )
    if is_binary == False:
        model = Word2Vec.load( path )
    else:
        model = keyedvectors.KeyedVectors.load_word2vec_format( path, binary=True )
    return model
