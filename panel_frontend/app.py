import dash
import dash_core_components as dcc
import dash_html_components as html
from src.layouts import ExternalStyles, HomeLayout, AdminLayout
from dash.dependencies import Input, Output, State
import requests
from flask import request
import pandas as pd
from src.configs import AppConfig
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    external_stylesheets=ExternalStyles,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
    suppress_callback_exceptions=True
)

external_script = "https://raw.githubusercontent.com/MarwanDebbiche/post-tuto-deployment/master/src/dash/assets/gtag.js"

app.scripts.append_script({
    "external_url": external_script
})


companies = pd.read_csv('src/csv/companies_forbes.csv')
random_reviews = pd.read_csv('src/csv/random_reviews.csv')

app.title = 'Nafi App'


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(
    [
        Output('company_logo', 'src'),
        Output('company_name', 'children'),
        Output('review', 'value'),
        Output('company_link', 'href')
    ],
    [
        Input('submit_button', 'n_clicks_timestamp'),
        Input('switch_button', 'n_clicks_timestamp')
    ],
    [
        State('review', 'value'),
        State('progress', 'value'),
        State('rating', 'value'),
        State('company_name', 'children')
    ]
)
def change_brand(submit_click_ts, another_brand_click_ts, review_text, score, rating, brand_name):
    if submit_click_ts > another_brand_click_ts:
        sentiment_score = float(score) / 100
        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent')
        response = requests.post(
            f"{AppConfig.API_URL}/review",
            data={
                'review': review_text,
                'rating': rating,
                'suggested_rating': min(int(sentiment_score * 5 + 1), 5),
                'sentiment_score': sentiment_score,
                'brand': brand_name,
                'user_agent': user_agent,
                'ip_address': ip_address
            }
        )

        if response.ok:
            print("Review Saved")
        else:
            print("Error Saving Review")

    random_company = companies.sample(1).to_dict(orient="records")[0]

    company_logo_url = random_company['company_logo']
    if not company_logo_url.startswith('http'):
        company_logo_url = 'https://' + company_logo_url

    company_name = random_company['company_name']
    company_website = random_company['company_website']

    return company_logo_url, company_name, '', company_website


@app.callback(
    [
        Output('proba', 'children'),
        Output('progress', 'value'),
        Output('progress', 'color'),
        Output('rating', 'value'),
        Output('submit_button', 'disabled')
    ],
    [Input('review', 'value')]
)
def update_proba(review):
    if review is not None and review.strip() != '':
        response = requests.post(
            f"{AppConfig.API_URL}/predict", data={'review': review})
        proba = response.json()
        proba = round(proba * 100, 2)
        suggested_rating = min(int((proba / 100) * 5 + 1), 5)
        text_proba = f"{proba}%"

        if proba >= 67:
            return text_proba, proba, 'success', suggested_rating, False
        elif 33 < proba < 67:
            return text_proba, proba, 'warning', suggested_rating, False
        elif proba <= 33:
            return text_proba, proba, 'danger', suggested_rating, False
    else:
        return None, 0, None, 0, True


# Load review table
@app.callback(
    Output('admin-page-content', 'children'),
    [Input('url', 'pathname')]
)
def load_review_table(pathname):
    if pathname != "/admin":
        return None

    response = requests.get(f"{AppConfig.API_URL}/reviews")

    reviews = pd.DataFrame(response.json())

    table = dbc.Table.from_dataframe(reviews,
                                     striped=True,
                                     bordered=True,
                                     hover=True,
                                     responsive=True,
                                     header=["id", "brand", "created_date", "review",
                                             "rating", "suggested_rating", "sentiment_score"],
                                     columns=["id", "brand", "created_date", "review",
                                              "rating", "suggested_rating", "sentiment_score"]
                                     )

    return table


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return HomeLayout.home_layout
    if pathname == "/admin":
        return AdminLayout.admin_layout
    else:
        return [
            html.Div(
                [
                    html.Img(
                        src="assets/404.png",
                        style={
                            "width": "50%"
                        }
                    ),
                ],
                className="form-review"
            ),
            dcc.Link("Go to Home", href="/"),
        ]


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8030)
