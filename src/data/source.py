from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pandas as pd

from ..data.loader import DataSchema
from .loader import DataSchema


@dataclass
class DataSource:
    _data: pd.DataFrame

