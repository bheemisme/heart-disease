import datetime as dt
from functools import partial, reduce
from typing import Callable


import pandas as pd

Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]


class DataSchema:
    index = "index"
    age = "age"
    sex = "sex"
    chest_pain = "cp"
    rest_blood_pressure = "trestbps"
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
    age_group = "age_group"


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=False)


def rename_gender(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.sex] = df[DataSchema.sex].map({0: 'Female', 1: "Male"})
    return df


def rename_target(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.target] = df[DataSchema.target].map(
        {1: 'Positive', 0: "Negative"})
    return df

def rename_exang(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.excercise_angina] = df[DataSchema.excercise_angina].map(
        {1: 'Positive', 0: "Negative"})
    return df


def rename_fbs(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.fasting_blood_sugar] = df[DataSchema.fasting_blood_sugar].map(
        {1: '>120 mg/dl', 0: "<120 mg/dl"})
    return df

def add_age_groups(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.age_group] = pd.cut(df[DataSchema.age], bins=[20, 30, 40, 50, 60, 70, 80])
    
    df[DataSchema.age_group] = pd.Series(list(map(lambda x: f'{x.left}-{x.right}', df[DataSchema.age_group])))
    return df



def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def load_data(path: str) -> pd.DataFrame:
    # load the data from the CSV file
    data = pd.read_csv(
        path
    )
    preprocessor = compose(
        remove_duplicates,
        rename_gender,
        rename_target,
        add_age_groups,
        rename_exang,
        rename_fbs
    )
    return preprocessor(data)
