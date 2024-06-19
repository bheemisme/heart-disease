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
    
    @property
    def slope(self):
        return self._data[DataSchema.slope].unique()
    
    @property
    def fbs(self):
        return self._data[DataSchema.fasting_blood_sugar].unique()
    
    def sorted_age_groups(self):
        groups = self._data[DataSchema.age_group].unique()
        groups.sort()
        return  groups
    