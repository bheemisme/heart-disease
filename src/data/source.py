from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .loader import DataSchema


@dataclass
class DataSource:
    _data: pd.DataFrame
    
    @property
    def df(self) -> pd.DataFrame:
        return self._data
    
    @property
    def target(self):
        return self._data[DataSchema.target].unique()
    
    @property
    def exang(self):
        return self._data[DataSchema.excercise_angina].unique()