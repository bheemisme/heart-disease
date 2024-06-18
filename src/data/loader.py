import datetime as dt
from functools import partial, reduce
from typing import Callable

import babel.dates
import pandas as pd

Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]



class DataSchema:
    age = "age"
    sex = "sex"
    chest_pain  = "cp"
    rest_blood_pressure="trestbps"
    cholestrol = "chol"
    fasting_blood_sugar = "fbs"
    resting_electrocardiographic_results = "restecg"
    max_heart_rate = "thalach"
    excercise_angina = "exang"
    oldpeak = "oldpeak"
    slope = "slope"
    major_vessels = "ca"
    thal = "thal"
    target = "target"
