# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/02_national/05_Experiments/99_merlion/06_Evaluate.ipynb.

# %% auto 0
__all__ = ['Evaluation']

# %% ../../../nbs/02_national/05_Experiments/99_merlion/06_Evaluate.ipynb 2
from typing import Optional,List
import logging
import sys
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from national.experiments.merlion.model import Model
from national.experiments.merlion.inference import Inference as  MerlionInference
from national.experiments.merlion import model
from national.experiments.merlion import data_splits 
from national.experiments.merlion.metrics import ForecastScoreAccumulator
from national.util.constants import PERCENTAGE_CONFIDENCE_INTERVAL

# %% ../../../nbs/02_national/05_Experiments/99_merlion/06_Evaluate.ipynb 3
logging.disable(sys.maxsize)

# %% ../../../nbs/02_national/05_Experiments/99_merlion/06_Evaluate.ipynb 4
class Evaluation(MerlionInference):

    def __init__(
        self,
        kpi: str,
        df: pd.DataFrame,
        freq: str,
        val_frac: float = 0.15,
        load_models: bool = False,
        **args,
    ):
        super().__init__(
            kpi=kpi,
            df=df,
            freq=freq,
            val_frac=val_frac,
            load_models=load_models,
            **args,
        )

        _models = [
            self.models.prophet,
            self.models.arima,
            self.models.mses,
            # self.models.ensemble,
            # self.models.partial_ensemble,
        ]

        if self.include_selector:
            _models = _models + [self.models.selector]

        _model: Model
        for _model in _models:

            if not _model.load_model:
                _model.evaluation.train = ForecastScoreAccumulator(
                    ground_truth=self.data.train,
                    predict=_model.forecast.train,
                )

        if len(self.data.val) > 0:

            for _model in _models:

                _model.evaluation.val = ForecastScoreAccumulator(
                    ground_truth=self.data.val,
                    predict=_model.forecast.val,
                )

