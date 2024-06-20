from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_alluvial1
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(dcc.Graph(
        figure=plot_alluvial1(source)),
        id=ids.ALLUVIAL_ONE
    )
