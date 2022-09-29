# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/02_national/04_TimeSeries/03_TrendSeasonalDecomposition.ipynb.

# %% auto 0
__all__ = ['decompose', 'plot_from_decompositions', 'plot']

# %% ../../nbs/02_national/04_TimeSeries/03_TrendSeasonalDecomposition.ipynb 2
from typing import Optional, Dict

from itertools import product as Product


import plotly.graph_objects as go
import numpy as np
import pandas as pd
import statsmodels.api as sm

from plotly.subplots import make_subplots
from national.util import constants
from national.time_series import process

# %% ../../nbs/02_national/04_TimeSeries/03_TrendSeasonalDecomposition.ipynb 3
def decompose(
    time_series: pd.DataFrame,
    model: str = 'additive',
):
    time_series = time_series.fillna(0)

    decomposition = sm.tsa.seasonal_decompose(time_series, model=model)

    return decomposition

# %% ../../nbs/02_national/04_TimeSeries/03_TrendSeasonalDecomposition.ipynb 4
def plot_from_decompositions(
    decompositions: Dict[str, pd.DataFrame],
    kpi: str,
    model: str = 'additive',
) -> make_subplots:
    """
    Given a time series it decompose it and plot the actual values, the trend, the residuals
    and the seasonal component. By default, it uses additive models
    
    :param time_series: A pandas dataframe with time series structure
    :param model: An indicator if the model is additive or multiplicative. Default 'Additive'
    :return: A subplot object with the time series decomposition.
    """

    colors = [
        'cornflowerblue',
        'darksalmon',
    ]

    fig = make_subplots(rows=2,
                        cols=2,
                        subplot_titles=("Observed", "Trend", "Resid",
                                        "Seasonal"))

    for color, freq in zip(colors, decompositions.keys()):

        decom = decompositions[freq]

        decomposition_array = [
            [decom.observed, decom.trend],
            [decom.resid, decom.seasonal],
        ]
        
        graph_name = freq + ' frequency'
        if freq.upper() in constants.PANDAS_FREQS.keys():
            graph_name = constants.PANDAS_FREQS[freq.upper()]

        for row, col in Product([1, 2], [1, 2]):

            decom = decomposition_array[row - 1][col - 1]
            showlegend: bool = row == 1 and col == 2

            fig.add_trace(go.Scatter(
                name=graph_name,
                x=decom.index,
                y=decom.values,
                hovertemplate="Date: %{x} <br>" + "Net Sales: $ %{y}",
                marker_color=color,
                showlegend=showlegend,
            ),
                          row=row,
                          col=col)

        title_text = f"Time Series Decomposition for {kpi.capitalize()}"

        fig.update_layout(
            height=500,
            autosize=True,
            title_text=title_text,
            showlegend=True,
            template=constants.PLOTLY_THEME,
        )

    return fig

# %% ../../nbs/02_national/04_TimeSeries/03_TrendSeasonalDecomposition.ipynb 5
def plot(
    df: pd.DataFrame,
    kpi: str,
    freqs: list = ['W-Fri', 'Q'],
    ylog: bool = True,
):
    

    # ts = df[kpi].resample('W-MON').mean()
    # ts.index.freq = 'W-MON'

    agg_method = {
        'price': np.mean,
        'min_price': np.mean,
        'max_price': np.mean,
    }
    

    ts = process.time_series(
        df=df,
        time_column='date',
        freq=freqs,
        agg_method=agg_method,
    )
    tsa_decomposition = {freq: decompose(ts[freq][kpi]) for freq in freqs}

    fig = plot_from_decompositions(
        tsa_decomposition,
        kpi=kpi,
    )

    return fig
