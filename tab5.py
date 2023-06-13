from dash import html, dcc
import plotly.graph_objects as go


def render_tab(df):
    chosen_plot = ["Age", "country", "Gender"]

    layout = html.Div(
        [
            html.H1("Klienci", style={"text-align": "center"}),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Dropdown(
                                id="clients_dropdown",
                                options=[
                                    {"label": what, "value": what}
                                    for what in chosen_plot
                                ],
                                value=chosen_plot[0],
                            ),
                            dcc.Graph(id="clients"),
                        ],
                        style={"width": "100%", "text-align": "center"},
                    ),
                ],
                style={"display": "flex"},
            ),
            html.Div(id="temp-out"),
        ]
    )

    return layout
