# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/02_national/01_DataPreprocessing/02_DateFeatures.ipynb.

# %% auto 0
__all__ = ['Data']

# %% ../../../nbs/02_national/01_DataPreprocessing/02_DateFeatures.ipynb 3
from . import load
from .. import tables
import pandas as pd

# %% ../../../nbs/02_national/01_DataPreprocessing/02_DateFeatures.ipynb 4
class Data(load.Data):

    def __init__(
            self,
            data_path: str = tables.granos_historico.version('04_W-MON'),
     ):
        super().__init__(data_path=data_path)

        self.df.set_index('date', inplace=True)

        self.df.sort_index(inplace=True)

        self.df['Year'] = self.df.index.year
        self.df['Month'] = self.df.index.month
        self.df[
            'WeekOfYear'] = self.df.index.isocalendar().week
        self.df.reset_index(inplace=True)
