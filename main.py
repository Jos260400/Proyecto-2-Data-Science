# Universidad del Valle de Guatemala
# Mineria de Datos
# HDT1-Exploratory Analysis
#------------------------------------
# Oliver de Leon 19270

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reader import reader as Reader

class main(object):

    def __init__(self, csvDoc):
        # Universal Doc
        self.csvDoc = csvDoc
        # Classes
        R = Reader(csvDoc)
        self.df = R.bundesLiga

  

exp = main('./data/train.csv')
# exp.Pricing_Boxplot()

