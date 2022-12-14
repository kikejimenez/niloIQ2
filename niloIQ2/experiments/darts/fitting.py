# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/02_national/05_Experiments/09_darts/03_Fit.ipynb.

# %% auto 0
__all__ = ['Fit']

# %% ../../../nbs/02_national/05_Experiments/09_darts/03_Fit.ipynb 2
import pandas as pd

from national.experiments.darts import model as darts_model
from national.experiments.darts import train_validation_test 

# %% ../../../nbs/02_national/05_Experiments/09_darts/03_Fit.ipynb 3
class Fit:

    def __init__(self,
    df: pd.DataFrame, 
    data_args: dict = {},
    models_args: dict = {},
    ) -> None:


        self.data = train_validation_test.Data(
              df=df, 
              **data_args,
            )

        self.models = darts_model.Models(**models_args)


        _models = [
            self.models.n_beats_model
        ]

        for _model in _models:
            _model.fit(self.data.train,verbose=True)

    
