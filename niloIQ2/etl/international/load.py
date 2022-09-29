# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/01_etl/00_InternationalPrices/01_LoadData.ipynb.

# %% auto 0
__all__ = ['USER', 'PASS', 'HOST', 'PORT', 'DB', 'sqlEngine', 'dbConnection', 'new_version']

# %% ../../../nbs/01_etl/00_InternationalPrices/01_LoadData.ipynb 2
from sqlalchemy import create_engine
from .. import tables

import pandas as pd
import os
import pathlib
from dotenv import load_dotenv

# %% ../../../nbs/01_etl/00_InternationalPrices/01_LoadData.ipynb 3
load_dotenv()

USER = os.getenv('USER')
PASS = os.getenv('PASS')
HOST = os.getenv('IP')
PORT = os.getenv('PORT')
DB = os.getenv('DB')

sqlEngine = create_engine(
    f'mysql+pymysql://{USER}:{PASS}@{HOST}/{DB}', pool_recycle=3600
)
dbConnection = sqlEngine.connect()


new_version ='01'

for table in tables.international_list:
    df = pd.read_sql(f"select * from {table.table_name}", dbConnection)
    df.to_csv(table.version(new_version),index=False)
    print(df.info)  
dbConnection.close()