from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_disease_dist
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(dcc.Graph(
        figure=plot_disease_dist(source)),
        id=ids.DISEASE_DIST)
