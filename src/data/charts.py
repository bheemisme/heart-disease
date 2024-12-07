
import seaborn as sns
import matplotlib.pyplot as plt
from .source import DataSource
from .loader import DataSchema

import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots


def plot_age_distribution(ds: DataSource) -> go.Figure:
    fig = px.histogram(
        data_frame=ds.df,
        x=DataSchema.age_group,
        color_discrete_sequence=["#3cc389"],
        histfunc="count",
        title="Age Distribution",
        category_orders={
            "age_group": ds.sorted_age_groups()
        }
    )
    fig.update_layout(yaxis_title="No. of patients", xaxis_title="Age")
    return fig


def plot_gender_pie_chart(ds: DataSource) -> go.Figure:
    gender_cnt = ds.df.groupby(by=[DataSchema.sex]).count()["index"].to_numpy()
    fig = px.pie(
        ds.df,
        names=["Female", "Male"],
        values=gender_cnt,
        title="Gender"
    )
    return fig


def plot_disease_dist(ds: DataSource) -> go.Figure:

    fig = px.histogram(ds.df,
                       x=DataSchema.sex,
                       color=DataSchema.target,
                       barmode="group",
                       histfunc="count",
                       category_orders={
                           "target": ["Positive", "Negative"]
                       },
                       labels={
                           "target": "Infected",
                           "sex": "Gender",
                           "count": "No. of patients",

                       },
                       title="Gender to Target"
                       )

    return fig


def plot_age_target(ds: DataSource) -> go.Figure:

    fig = px.histogram(ds.df,
                       x=DataSchema.age_group,
                       color=DataSchema.target,
                       histfunc="count",
                       category_orders={
                           "age_group": ds.sorted_age_groups()
                       },
                       labels={
                           "age_group": "Age",
                           "target": "Infected"
                       },
                       title="Age to target"
                       )

    return fig


def plot_chol_target(ds: DataSource) -> go.Figure:

    fig = px.violin(ds.df,
                    x=DataSchema.target,
                    y=DataSchema.cholestrol,
                    title="Target - Cholestrol"
                    )
    fig.update_layout(
        xaxis_title="Target",
        yaxis_title="Cholestrol"
    )
    return fig  # type: ignore


# clean the outliers
def plot_heart_rate_age(ds: DataSource) -> go.Figure:
    pivot = ds.df[(ds.df[DataSchema.age] >= 30) &
                  (ds.df[DataSchema.age] <= 70)]
    fig = px.scatter(pivot,
                     x=DataSchema.age,
                     y=DataSchema.max_heart_rate,
                     color=DataSchema.target,
                     title="Age - Heart Rate"
                     )
    fig.update_layout(xaxis_title="Age", yaxis_title="Max Heart Rate")

    return fig


def plot_gender_cp(ds: DataSource) -> go.Figure:
    pivot = ds.df[(ds.df[DataSchema.age] >= 30) &
                  (ds.df[DataSchema.age] <= 70)]

    fig = px.histogram(pivot,
                       x=DataSchema.sex,
                       color=DataSchema.chest_pain,
                       histfunc="count",
                       barmode="group",
                       labels={
                           "cp": "chest pain"
                       },
                       title="Gender to chestpain"
                       )

    return fig


def plot_cp(ds: DataSource) -> go.Figure:
    pivot = ds.df[(ds.df[DataSchema.age] >= 30) &
                  (ds.df[DataSchema.age] <= 70)]

    fig = px.histogram(pivot,
                       x=DataSchema.target,
                       color=DataSchema.chest_pain,
                       histfunc="count",
                       barmode="group",
                       labels={
                           "cp": "chest pain"
                       },
                       title="Chestpain"
                       )
    return fig


def plot_oldpeak_age(ds: DataSource) -> go.Figure:
    fig = px.histogram(ds.df,
                       x=DataSchema.age_group,
                       y=DataSchema.oldpeak,

                       histfunc="avg",
                       category_orders={
                           "age_group": ds.sorted_age_groups()

                       },
                       labels={
                           "age_group": "Age"
                       },
                       title="Average Oldpeak Age"
                       )
    return fig


def plot_angina_target(ds: DataSource) -> go.Figure:
    z = ds.df.groupby(by=[DataSchema.excercise_angina,
                      DataSchema.target]).count()["index"]
    z = z.to_numpy().reshape((len(ds.exang), len(ds.target)))
    fig = go.Figure(data=[go.Heatmap(
        x=ds.target,
        y=ds.exang,
        z=z,
        colorscale="Greens"
    )])
    fig.update_layout(xaxis_title='Target',
                      yaxis_title="Exercise induced angina",
                      title_text="Angina - Target"
                      )
    return fig


def plot_slope_target(ds: DataSource) -> go.Figure:

    fig = px.histogram(ds.df, x=DataSchema.slope,
                       color=DataSchema.target,
                       histfunc="count",
                       barmode="group",
                       color_discrete_sequence=px.colors.qualitative.Pastel
                       )
    fig.update_layout(
        xaxis_title='Slope',
        yaxis_title="No. of patients",
        title_text="Slope - Target"
    )

    return fig


def plot_slope_exang(ds: DataSource) -> go.Figure:

    fig = px.histogram(ds.df,
                       x=DataSchema.slope,
                       color=DataSchema.excercise_angina,
                       histfunc="count",
                       barmode="group",
                       color_discrete_sequence=px.colors.qualitative.Pastel
                       )
    fig.update_layout(
        xaxis_title='Slope',
        yaxis_title="No. of patients",
        title_text="Slope - Exang"
    )

    return fig


def plot_fbs_target(ds: DataSource) -> go.Figure:

    fig = px.histogram(ds.df,
                       x=DataSchema.fasting_blood_sugar,
                       color=DataSchema.target,
                       histfunc="count",
                       barmode="group",
                       color_discrete_sequence=px.colors.qualitative.Safe,
                       title="Fasting Blood Sugar - Patients"
                       )
    fig.update_layout(
        xaxis_title="Fasting Blood Sugar",
        yaxis_title="No. of patients"
    )

    return fig


def plot_heart_rate(ds: DataSource) -> go.Figure:

    fig = px.violin(data_frame=ds.df,
                 x=DataSchema.target,
                 y=DataSchema.max_heart_rate,
                 color_discrete_sequence=px.colors.qualitative.Vivid,
                 title="Target - Max Heart Rate"
                 )
    fig.update_layout(
        xaxis_title="Target",
        yaxis_title="Max Heart Rate"
    )

    return fig


def plot_fbs_thalach(ds: DataSource) -> go.Figure:

    fig = px.violin(data_frame=ds.df,
                 x=DataSchema.fasting_blood_sugar,
                 y=DataSchema.max_heart_rate,
                 color_discrete_sequence=px.colors.qualitative.Vivid,
                 title="Fasting Blood Sugar - Max Heart Rate"
                 )
    fig.update_layout(
        xaxis_title="Fasting Blood Sugar",
        yaxis_title="Max Heart Rate"
    )

    return fig


def plot_rcg_target(ds: DataSource) -> go.Figure:

    fig = px.histogram(ds.df,
                       x=DataSchema.resting_electrocardiographic_results,
                       color=DataSchema.target,
                       color_discrete_sequence=px.colors.qualitative.Vivid,
                       title="Resting ECG - Target",
                       barmode="group"
                       )
    fig.update_layout(
        xaxis_title="Resting ECG",
        yaxis_title="No. of patients"
    )

    return fig

