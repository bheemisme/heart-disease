from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_heart_rate
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
    
    return html.Div(dcc.Graph(figure=plot_heart_rate(source)),
        id=ids.HEART_RATE,
        className="w-50"
        )
