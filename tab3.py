from dash import html, dcc
import plotly.graph_objects as go


def render_tab(df):
    grouped = df[df["total_amt"] > 0].groupby("Store_type")["total_amt"].count()
    fig = go.Figure(
        data=[go.Pie(labels=grouped.index, values=grouped.values)],
        layout=go.Layout(title="Kanały sprzedaży/liczba transakcji"),
    )

    layout = html.Div(
        [
            html.H1("Kanały sprzedaży", style={"text-align": "center"}),
            html.Div(
                [
                    html.Div(
                        [dcc.Graph(id="pie-Store-type", figure=fig)],
                        style={"width": "50%"},
                    ),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id="store_dropdown",
                                options=[
                                    {"label": Store_type, "value": Store_type}
                                    for Store_type in df["Store_type"].unique()
                                ],
                                value=df["Store_type"].unique()[0],
                            ),
                            dcc.Graph(id="barh-Store-type"),
                        ],
                        style={"width": "50%"},
                    ),
                ],
                style={"display": "flex"},
            ),
            html.Div(id="temp-out"),
        ]
    )

    return layout
