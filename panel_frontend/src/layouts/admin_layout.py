import dash_core_components as dcc
import dash_html_components as html


class AdminLayout:
    admin_layout = html.Div(
        [
            html.H1("Admin Page 🔑"),
            html.Div(id="admin-page-content"),
            html.P(
                dcc.Link("Go to Home 🏡", href="/"),
                style={"marginTop": "20px"}
            )
        ]
    )