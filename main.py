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
        #print(self.df)
    # Entrada de eventos por video
    def entry_amount_per_video(self):
        df = self.df
        df = df.groupby('video_id').size().to_frame('count')
        #print(df.mean())
        """
        df = df.sort_values('count', ascending=False)
        ax = df.plot.bar(y = 'count', use_index=True)
        plt.title('Entries amount per video')
        plt.ylabel('Amount of entries')
        plt.xlabel('Video ID')
        plt.show()
        """
    # Entrada de eventos por video
    def event_amount_per_video(self):
        df = self.df
        df = self.df[df['event'] == 'end']
        df = df[['event', 'video_id']]
        df = df.groupby('video_id').count()
        #print(df.mean())
        """
        df = df.sort_values('event', ascending=False)
        ax = df.plot.bar(use_index=True)
        plt.title('Completed events per video')
        plt.ylabel('Amount of completed events')
        plt.xlabel('Video ID')
        plt.show()
        """


exp = main('./data/train.csv')
exp.event_amount_per_video()

