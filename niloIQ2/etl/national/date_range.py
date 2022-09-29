# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/01_etl/00_NationalPrices/98_DateRange.ipynb.

# %% auto 0
__all__ = ['table']

# %% ../../../nbs/01_etl/00_NationalPrices/98_DateRange.ipynb 2
import pandas as pd
from .. import tables

# %% ../../../nbs/01_etl/00_NationalPrices/98_DateRange.ipynb 3
table:tables.Table

for version in ('02',):
    for table in tables.national_list:
        data = pd.read_csv(table.version(version),low_memory=False,)
        ts = pd.to_datetime(data['fecha'])

        min_date = ts.min()
        max_date = ts.max()
        range_date = max_date - min_date

        print(
        f"""
        For table {table.version(version)}:
            The time frame starts on {min_date.strftime('%Y-%m-%d')} and conclude on {max_date.strftime('%Y-%m-%d')}. A total of {range_date.days} days"""
        )
