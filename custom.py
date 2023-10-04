import pandas as pd
import numpy as np
import joblib
from sklearn.base import BaseEstimator,TransformerMixin

class CustomTransformer_cat(BaseEstimator, TransformerMixin):    
        def __init__(self):
            print('\n>>>>>>>init() called.\n')
            pass
        def fit(self, X, y = None):
            return self
        def transform(self, X, y = None):
            X['Name'] = X['Name'].apply(lambda x:x.split(' ')[1])
            X['Year'] = X['Year'].astype(str)
            X['Year'] = X['Year'].str.slice(0,4)
            return X
        
