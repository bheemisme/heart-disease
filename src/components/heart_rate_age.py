from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_heart_rate_age
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
    
    return html.Div(dcc.Graph(figure=plot_heart_rate_age(source)),
        id=ids.HEART_RATE_AGE,className="w-50")
