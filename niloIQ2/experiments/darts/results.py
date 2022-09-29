# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/02_national/05_Experiments/09_darts/07_Results.ipynb.

# %% auto 0
__all__ = ['Results']

# %% ../../../nbs/02_national/05_Experiments/09_darts/07_Results.ipynb 2
from typing import List

import logging
import sys
import pandas as pd
import plotly.graph_objects as go

from national.util.constants import PERCENTAGE_CONFIDENCE_INTERVAL

from national.experiments.darts import predict, evaluate
from national.util import constants

# %% ../../../nbs/02_national/05_Experiments/09_darts/07_Results.ipynb 3
logging.disable(sys.maxsize)

# %% ../../../nbs/02_national/05_Experiments/09_darts/07_Results.ipynb 4
def _confidence_interval(
    pred: pd.Series,
    stderr: pd.Series,
    percentage_interval,
):

    k = PERCENTAGE_CONFIDENCE_INTERVAL[percentage_interval]

    upper_bound = pred + k * stderr
    lower_bound = pred - k * stderr

    return upper_bound, lower_bound

# %% ../../../nbs/02_national/05_Experiments/09_darts/07_Results.ipynb 5
def _metrics(
    models: List[model.Model],
    is_train: bool = True,
):

    _index = pd.Index([x.name for x in models], name='Model')

    if is_train:
        _evaluations = [model.evaluation.train for model in models]
    else:

        _evaluations = [model.evaluation.val for model in models]

    df = pd.DataFrame(
        {
            'sMAPE': [x.smape() for x in _evaluations],
            'rRSME': [x.rrmse() for x in _evaluations],
            'RMSPE': [x.rmspe() for x in _evaluations],
        },
        index=_index,
    )

    df['Dataset'] = 'Train' if is_train else 'Validation'
    return df.reset_index().set_index(['Dataset', 'Model'])

# %% ../../../nbs/02_national/05_Experiments/09_darts/07_Results.ipynb 6
class Results(Predict):

    def __init__(
        self,
        **args,
    ):
        super().__init__(**args)

    def plot_model(
        self,
        model: model.Model,
    ):

        return _plot(
            data=self.data,
            model=model,
            freq=self.freq,
            kpi=self.kpi,
            start_at=2,
        )

    def metrics(
        self,
        is_train: bool = True,
    ):
        models = [
            self.models.arima,
            self.models.prophet,
            self.models.mses,
            self.models.partial_ensemble,
        ]
        return _metrics(
            models=models,
            is_train=is_train,
        )