from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_alluvial2
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(dcc.Graph(
        figure=plot_alluvial2(source)),
        id=ids.ALLUVIAL_TWO
    )
