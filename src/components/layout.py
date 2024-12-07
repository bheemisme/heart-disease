from dash import Dash, html
from ..data.source import DataSource

from src.components import (
    age_dist,
    gender_pie,
    disease_dist,
    chest_pain,
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
    slope_exang,
    heart_rate
)


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title, className="text-center text-primary"),
            html.Div(className="body-container", children=[
                html.Nav(className="navbar", children=[]),
                html.Div(className="chart-container d-flex flex-column align-items-center", children=[
                    html.Div(className="d-flex flex-row align-items-center justify-content-between",
                             children=[
                                 age_dist.render(app, source),
                                 gender_pie.render(app, source),
                             ]),
                    html.Div(children=[
                        disease_dist.render(app, source),
                        target_age.render(app, source),
                        chest_pain.render(app, source),
                        gender_cp.render(app, source),
                        heart_rate_age.render(app, source),
                        chol_target.render(app, source),
                        oldpeak_age.render(app, source),
                        angina_target.render(app, source),
                        slope_target.render(app, source),
                        slope_exang.render(app, source),
                        fbs_target.render(app, source),
                        fbs_thalach.render(app, source),
                        heart_rate.render(app, source),
                        rcg_target.render(app, source)

                    ], className="d-flex flex-row flex-wrap justify-content-between align-items-center")
                ])

            ])
        ],
    )
