# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/02_national/05_Experiments/09_darts/05_Predict.ipynb.

# %% auto 0
__all__ = ['Predictions', 'Predict', 'plot']

# %% ../../../nbs/02_national/05_Experiments/09_darts/05_Predict.ipynb 2
from typing import Optional,List

import pandas as pd


import plotly.graph_objects as go

from darts.dataprocessing.transformers import Scaler
from darts.timeseries import TimeSeries
from national.experiments.darts import fitting 


from national.util import constants 

# %% ../../../nbs/02_national/05_Experiments/09_darts/05_Predict.ipynb 3
class Predictions:
    def __init__(self) -> None:
        self.n_beats = None

# %% ../../../nbs/02_national/05_Experiments/09_darts/05_Predict.ipynb 4
class Predict(fitting.Fit):

    default_horizons = dict(n_beats=36, )

    def __init__(
        self, df: pd.DataFrame, horizons: dict = default_horizons, **args
    ):
        super().__init__(
            df=df,
            **args,
        )

        self.predictions = Predictions()

        self.predictions.n_beats = self.models.n_beats_model.predict(
            len(self.data.val),
        )

# %% ../../../nbs/02_national/05_Experiments/09_darts/05_Predict.ipynb 7
def _descalate(scaler:Scaler,
  ts_list: List[TimeSeries],
) -> pd.Series:

   inv = scaler.inverse_transform

   _ts_list = [scaler.inverse_transform(ts) for ts in ts_list]
    
   return [
      ts._xa.to_series().reset_index(level=[1,2],)[0]
    for ts in _ts_list] 

# %% ../../../nbs/02_national/05_Experiments/09_darts/05_Predict.ipynb 8
def plot(preds: Predict, ):
    ...
    data = preds.data
    ts, ts_pred = _descalate(
        scaler= preds.data.scaler,
        ts_list = [preds.data.time_series, preds.predictions.n_beats],
    )
  
    # ts = preds.data.scaler.inverse_transform(data.time_series)

    # ts_pred = preds.data.scaler.inverse_transform(preds.predictions.n_beats)

    # ts = ts._xa.to_series().reset_index(level=[1,2],)[0]
    #val = data.val._xa.to_series().reset_index(level=[1,2])[0]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            name=f"Actual",
            x=ts.index,
            y=ts.values,
            marker_color='cornflowerblue',
            showlegend=True,
        ),
    )

    fig.add_trace(
        go.Scatter(
            name=f"Forecast",
            x=ts_pred.index,
            y=ts_pred.values,
            marker_color='LightSalmon',
            showlegend=True,
        ),
    )

    return fig