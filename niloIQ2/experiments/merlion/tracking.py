# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/02_national/05_Experiments/99_merlion/08_Tracking.ipynb.

# %% auto 0
__all__ = ['Tracking']

# %% ../../../nbs/02_national/05_Experiments/99_merlion/08_Tracking.ipynb 2
import os
import warnings
import sys
import logging

from urllib.parse import urlparse

import pandas as pd
import mlflow

from national import tables
from national.experiments.merlion.results import Results
from national.data_preprocessing.date_features import Data

# %% ../../../nbs/02_national/05_Experiments/99_merlion/08_Tracking.ipynb 3
from ensurepip import version
from genericpath import isfile


class Tracking(Results):

    def __init__(
        self,
        # df: pd.DataFrame,
        kpi: str,
        freq: str,
        load_models: bool,
        periods: int,
        val_frac: float,
        since_year: int,
        state: str,
        product: str,
        **args,
    ):

        self.query = "Year>={} & product=='{}' & state=='{}'".format(
            since_year,
            product,
            state,
        )
        super().__init__(
            df=Data().df.query(self.query),
            kpi=kpi,
            freq=freq,
            load_models=load_models,
            periods=periods,
            val_frac=val_frac,
            # query=query,
            **args,
        )

        logging.basicConfig(level=logging.WARN)
        logger = logging.getLogger(__name__)

        self.local_uri = 'file:///workspaces/niloIQ/data/NationalPrices/mlruns'

        # mlflow.set_experiment_tag("release.version", "2.2.0")
        mlflow.set_tracking_uri(uri=self.local_uri)

        self.exp_name = 'National'

        try:
            exp = mlflow.get_experiment_by_name(name=self.exp_name)
            experiment_id = exp.experiment_id
        except:

            experiment_id = mlflow.create_experiment(
                name=self.exp_name,
                artifact_location=self.local_uri,
            )

        _metrics = self.metrics()
        _preds = self.get_futures_dict()

        for _dataset, model in _metrics.index.values:
            with mlflow.start_run(
                    experiment_id=experiment_id,
                    run_name='Merlion',
            ):

                warnings.filterwarnings("ignore")
            


                mlflow.log_param("kpi", self.kpi)
                mlflow.log_param("freq", self.freq)
                mlflow.log_param("model", model)
                mlflow.log_param("product", product)
                mlflow.log_param("since_year", since_year)
                mlflow.log_param("state", state)
                mlflow.log_param("pred_start_date",self.data.futuristic_start_date )
                mlflow.log_param("predictions", str(_preds[model]))

                _query = _metrics.query(
                    f"Dataset=='{_dataset}' & Model=='{model}'")
                mlflow.log_metric(f"sMAPE", _query['sMAPE'].values[0])
                mlflow.log_metric(f"rRSME", _query['rRSME'].values[0])
                mlflow.log_metric(f"RMSPE", _query['RMSPE'].values[0])

        runs = mlflow.search_runs(experiment_names=[self.exp_name])

        _file =tables.granos_actual.version("merlion")

        if os.path.isfile(_file):
            runs.to_csv(_file,mode='a',header=False,index=False)
        else:
            runs.to_csv(_file,mode='w',index=False)