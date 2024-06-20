from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_rcg_thalach
from . import ids

def render(app: Dash, source: DataSource) -> html.Div:
    
    return html.Div(
        dcc.Graph(figure=plot_rcg_thalach(source)),
        id=ids.RCG_THALACH,
        className="")