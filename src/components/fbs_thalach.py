from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_fbs_thalach
from . import ids

import plotly.express as px


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_fbs_thalach(source)),
        id=ids.FBS_THALACH
    )
