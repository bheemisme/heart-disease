from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_slope_exang
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_slope_exang(source)),
        id=ids.SLOPE_EXANG,
        className="w-50"
    )
