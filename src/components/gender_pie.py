from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_gender_pie_chart
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
    
    return html.Div(dcc.Graph(figure=plot_gender_pie_chart(source)),
        id=ids.GENDER_PIE,className="w-50")
