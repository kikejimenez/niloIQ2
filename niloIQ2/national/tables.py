# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/02_national/98_Tables.ipynb.

# %% auto 0
__all__ = ['ROOT_DIRECTORY', 'AMS_PRECIOS_INTERNACIONALES_PUNTO_DE_EMBARQUE_ACTUAL',
           'AMS_PRECIOS_INTERNACIONALES_PUNTO_DE_EMBARQUE_HISTORICA', 'SNIIM_GRANOS_BASICOS_ACTUAL',
           'SNIIM_GRANOS_BASICOS_HISTORICA', 'granos_actual', 'granos_historico', 'precios_internacionales_actual',
           'precios_internacionales_historico', 'national_list', 'international_list', 'table_list', 'table_dict',
           'Table']

# %% ../../nbs/02_national/98_Tables.ipynb 2
from pathlib import Path
import os
from os import path,mkdir

ROOT_DIRECTORY = '/workspaces/niloIQ2'

AMS_PRECIOS_INTERNACIONALES_PUNTO_DE_EMBARQUE_ACTUAL = os.getenv(
    'AMS_PRECIOS_INTERNACIONALES_PUNTO_DE_EMBARQUE_ACTUAL'
)
AMS_PRECIOS_INTERNACIONALES_PUNTO_DE_EMBARQUE_HISTORICA = os.getenv(
    'AMS_PRECIOS_INTERNACIONALES_PUNTO_DE_EMBARQUE_HISTORICA'
)
SNIIM_GRANOS_BASICOS_ACTUAL = os.getenv('SNIIM_GRANOS_BASICOS_ACTUAL')
SNIIM_GRANOS_BASICOS_HISTORICA = os.getenv('SNIIM_GRANOS_BASICOS_HISTORICA')


class Table:
    def __init__(
        self,
        name: str,
        parent_dir: str = '',
    ) -> None:
        self.table_name = name
        self.parent_dir = parent_dir

    def version(
        self,
        version_name: str,
    ) -> str:

        
        _dir = path.join(ROOT_DIRECTORY, self.parent_dir, version_name)
        if not path.isdir(_dir):
            mkdir(_dir)
        return path.join(_dir, self.table_name)


granos_actual = Table(
    "sniim_granosbasicos",
    parent_dir='data/NationalPrices',
)
granos_historico = Table(
    "sniim_granosbasicoshistorica",
    parent_dir="data/NationalPrices",
)
precios_internacionales_actual = Table(
    "ams_preciosinternacionalespuntoembarque",
    parent_dir="data/InternationalPrices",
)
precios_internacionales_historico = Table(
    "ams_preciosinternacionalespuntoembarquehistorica",
    parent_dir="data/InternationalPrices",
)

national_list = [
    granos_actual,
    granos_historico,
]

international_list = [
    precios_internacionales_actual,
    precios_internacionales_historico,
]

table_list = [
    granos_actual,
    granos_historico,
    precios_internacionales_actual,
    precios_internacionales_historico,
]

table_dict = {
    "granos_actual": granos_actual,
    "granos_historico": granos_historico,
    "internacionales_actual": precios_internacionales_actual,
    "internacionales_historico": precios_internacionales_historico,
}
