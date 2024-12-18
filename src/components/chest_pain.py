from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_cp
from . import ids

import plotly.express as px


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_cp(source)),
        id=ids.CHEST_PAIN,
        className="w-50"
    )
