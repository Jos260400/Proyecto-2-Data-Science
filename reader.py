# Libs
import pandas as pd

"""
Universidad del Valle de Guatemala
Author: Oliver Milian
Purpose: CSV loader
"""
class reader(object):
    # Loads the CSV doc
    def __init__(self, csvDoc):
        self.bundesLiga = pd.read_csv(csvDoc, encoding= 'unicode_escape')

