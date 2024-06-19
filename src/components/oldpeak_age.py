from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_oldpeak_age
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_oldpeak_age(source)),
        id=ids.OLDPEAK_AGE,
        className=""
    )
