from dash import Dash, html
from ..data.source import DataSource

from src.components import (
    age_dist,
    alluvial1,
    gender_pie,
    disease_dist,
    gender_cp,
    chol_target,
    target_age,
    heart_rate_age,
    oldpeak_age,
    angina_target,
    slope_target,
    fbs_target,
    fbs_thalach,
    rcg_target,
    rcg_thalach,
    alluvial2
)


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title, className="text-center text-primary"),
            html.Div(className="body-container", children=[
                html.Nav(className="navbar", children=[

                    html.Span("Navbar", className="nav-item"),
                    html.Span("Navbar", className="nav-item"),
                    html.Span("Navbar", className="nav-item"),
                ]),
                html.Div(className="chart-container d-flex flex-column align-items-center", children=[
                    html.Div(className="d-flex flex-column align-items-center justify-content-center",
                             children=[
                                 age_dist.render(app, source)
                             ]),
                    html.Div(children=[
                        gender_pie.render(app, source),
                        disease_dist.render(app, source),
                        target_age.render(app, source),
                        heart_rate_age.render(app, source),
                        gender_cp.render(app, source),
                        chol_target.render(app, source),

                        oldpeak_age.render(app, source),
                        angina_target.render(app, source),
                        slope_target.render(app, source),
                        fbs_target.render(app, source),
                        fbs_thalach.render(app, source),
                        rcg_target.render(app, source),
                        rcg_thalach.render(app, source),

                    ], className="d-flex flex-row flex-wrap"),
                    html.Div(children=[
                        alluvial1.render(app, source),
                        alluvial2.render(app, source),
                    ], className="d-flex flex-row align-items-center justify-content-center")
                ])

            ])
        ],
    )
