# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/02_national/05_Experiments/99_merlion/03_Training.ipynb.

# %% auto 0
__all__ = ['Train']

# %% ../../../nbs/02_national/05_Experiments/99_merlion/03_Training.ipynb 2
import pandas as pd
from national.experiments.merlion import model as merlion_model
from national.experiments.merlion import data_splits

# %% ../../../nbs/02_national/05_Experiments/99_merlion/03_Training.ipynb 3
class Train():

    def __init__(
        self,
        kpi: str,
        freq: str,
        df: pd.DataFrame,
        load_models: bool = False,
        val_frac: float = 0.15,
        **args,
    ):
        # super().__init__()

        self.data = data_splits.Data(
            kpi=kpi,
            df=df,
            freq=freq,
            val_frac=val_frac,
            **args,
        )

        self.kpi = kpi
        self.freq = freq

        self.include_selector = 'D' in freq and len(freq) > 1 and int(
            freq[0]) < 7

        self.models = merlion_model.Models(
            granularity=freq,
            load_models=load_models,
        )

        _models = [
            self.models.arima,
            self.models.prophet,
            self.models.mses,
            # self.models.ensemble,
            # self.models.partial_ensemble
        ]
        if self.include_selector:
            _models.append(self.models.selector)

        for _model in _models:
            if not _model.load_model:
                print(_model.name)

                forecast, stderr = _model.model.train(self.data.train, )
                _model.forecast.train = forecast
                _model.stderr.train = stderr
