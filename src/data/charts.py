
import seaborn as sns
import matplotlib.pyplot as plt
from .source import DataSource
from .loader import DataSchema
from plotly.tools import mpl_to_plotly

import plotly.express as px
import plotly.graph_objects as go


def plot_age_distribution(ds: DataSource) -> go.Figure:
    sns.set_theme("notebook")
    sns.set_style("darkgrid")
    plt.title("Age Distribution")
    g = sns.histplot(ds.df,
                     x=DataSchema.age,
                     color="g",
                     bins=10,
                     kde=True,
                     stat="count",
                     cumulative=False
                     )

    fig = g.get_figure()
    return mpl_to_plotly(fig, resize=True)  # type: ignore


def plot_gender_pie_chart(ds: DataSource) -> go.Figure:
    gender_cnt = ds.df.groupby(by=[DataSchema.sex]).count()["index"].to_numpy()
    fig = px.pie(ds.df, names=["Female", "Male"],
                 values=gender_cnt, title="Gender")
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
    i = ds.df[DataSchema.age_group].unique()
    i.sort()
    fig = px.histogram(ds.df,
                       x=DataSchema.age_group,
                       color=DataSchema.target,
                       histfunc="count",
                       category_orders={
                           "age_group": i
                       },
                       labels={
                           "age_group": "Age",
                           "target": "Infected"
                       },
                       title="Age to target"
                       )
    return fig


def plot_gender_cp(ds: DataSource) -> go.Figure:
    fig = px.histogram(ds.df,
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

# clean the outliers


def plot_chol_target(ds: DataSource) -> go.Figure:
    fig = px.histogram(ds.df,
                       x=DataSchema.target,
                       y=DataSchema.cholestrol,
                       barmode="group",
                       histfunc="avg",
                       title="Target - Cholestrol"
                       )
    fig.update_layout(xaxis_title="Target", yaxis_title="Average Cholestrol")
    return fig  # type: ignore


# clean the outliers
def plot_heart_rate_age(ds: DataSource) -> go.Figure:
    fig = px.scatter(ds.df,
                     x=DataSchema.age,
                     y=DataSchema.max_heart_rate,
                     color=DataSchema.target,
                     title="Age - Heart Rate"
                     )
    fig.update_layout(xaxis_title="Age", yaxis_title="Max Heart Rate")
    
    return fig


def plot_oldpeak_age(ds: DataSource) -> go.Figure:
    i = ds.df[DataSchema.age_group].unique()
    i.sort()
    fig = px.histogram(ds.df,
                       x=DataSchema.age_group,
                       y=DataSchema.oldpeak,

                       histfunc="avg",
                       category_orders={
                           "age_group": i
                       }
                       )
    return fig


def plot_angina_target(ds: DataSource) -> go.Figure:
    z = ds.df.groupby(by=[DataSchema.excercise_angina, DataSchema.target]).count()["index"]
    z = z.to_numpy().reshape((len(ds.exang), len(ds.target)))
    fig = go.Figure(data=[go.Heatmap(
        x=ds.target,
        y=ds.exang,
        z=z,
        colorscale="Greens"
    )])
    fig.update_layout(xaxis_title='Infected',yaxis_title= "Exercise induced angina")
    return fig

