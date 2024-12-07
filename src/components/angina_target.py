from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_angina_target
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(dcc.Graph(
        figure=plot_angina_target(source)),
        id=ids.ANGINA_TARGET, 
        className='w-50'
    )
