from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_age_target
from . import ids



def render(app: Dash, source: DataSource) -> html.Div:
    
    return html.Div(
        dcc.Graph(figure=plot_age_target(source)),
        id=ids.AGE_CP,
        className="")