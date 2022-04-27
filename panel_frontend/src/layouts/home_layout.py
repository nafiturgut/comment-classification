

import sys

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from src.configs import AppConfig

sys.path.append(".")


class HomeLayout:
    home_layout = html.Div(
        [
            html.Div(
                [
                    html.A(
                        html.Img(
                            id='company_logo',
                            style={
                                'height': '100px',
                                'padding': '5px'
                            }
                        ),
                        id="company_link",
                        target="_blank"
                    )
                ],
                style={
                    'height': '100px',
                    'backgroundColor': 'white',
                    'borderStyle': 'solid',
                    'borderRadius': '100px',
                    'borderWidth': 'thin'
                }
            ),
            html.Br(),
            dcc.Dropdown(
                id='select_brand',
                options=[
                    {'label': 'Boran', 'value': 'Banabi'},
                    {'label': 'Nafi', 'value': 'Getir'},
                    {'label': 'Memo', 'value': 'Migros'}
                ],
                value='Getir'
            ),
            html.H1(
                [

                    html.Span(
                        id='company_name'
                    ),
                    " hakkında ne düşünüyorsunuz?"
                ],
                className="h3 mb-3 font-weight-normal",
                style={
                    'marginTop': '5px'
                }
            ),

            html.Div(
                [
                    dcc.Textarea(
                        className="form-control z-depth-1",
                        id="review",
                        rows="8",
                        placeholder="Hintli coder borovski :)..."
                    )
                ],
                className="form-group shadow-textarea"
            ),

            html.H5(
                'Metin Analizi 🤖'
            ),

            dbc.Progress(
                children=html.Span(
                    id='proba',
                    style={
                        'color': 'black',
                        'fontWeight': 'bold'
                    }
                ),
                id="progress",
                striped=False,
                animated=False,
                style={
                    'marginBottom': '10px'
                }
            ),

            html.H5(
                'Puan ver 😁📢'
            ),

            html.Div(
                [
                    dcc.Slider(
                        id='rating',
                        max=5,
                        min=1,
                        step=1,
                        marks={i: f'{i}' for i in range(1, 6)}
                    ),
                ],
                style={'marginBottom': '30px'}
            ),

            html.Button(
                [
                    html.Span(
                        "Kaydet",
                        style={
                            "marginRight": "10px"
                        }
                    ),
                    html.I(
                        className="fa fa-paper-plane m-l-7"
                    )
                ],
                className="btn btn-lg btn-primary btn-block",
                role="submit",
                id="submit_button",
                n_clicks_timestamp=0
            ),
            html.Button(
                [
                    html.Span(
                        "Şirket Değiştir",
                        style={
                            "marginRight": "10px"
                        }
                    ),
                    html.I(
                        className="fas fa-sync-alt"
                    )
                ],
                className="btn btn-lg btn-secondary btn-block",
                id='switch_button',
                n_clicks_timestamp=0
            ),
            html.P(
                dcc.Link("Go to Admin 🔑", id="admin-link", href="/admin"),
                className="mt-2"

            ),
            html.P(
                [
                    html.A("RefRef", href=AppConfig.NAT_LINKEDIN, target="_blank"),
                    " - 2020"
                ],
                className="mt-3 mb-2 text-muted"
            ),
        ],
        className="form-review",
    )