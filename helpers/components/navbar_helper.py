import dash_html_components as html
import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    html.H1("NBA", className="nba"),
                    href="https://www.nba.com/",
                    target="blank",
                    # style={"paddingTop": "15%"}
                ),

                className="nba-logo-img",
                style={"display": "flex", "align-items": "baseline"}
            ),

            dbc.NavItem(
                dbc.NavLink(
                    html.H1("Hoops"),
                ),
                style={"display": "flex", "align-items": "baseline"}
            ),

            dbc.NavItem(
                dbc.NavLink(
                    html.H1("Draft Board", className="nba"),
                    href="/apps/draft",
                ),
                style={"display": "flex", "align-items": "baseline"}
            ),

            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem(i, id=i)
                    for i in sorted(
                        ["All Teams", "Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"]
                    )
                ],
                nav=True,
                label="All Teams",
                id="team-list",
                in_navbar=True,
                className="dropdown",
            ),

            dbc.NavItem(
                dbc.NavLink(
                    html.H1("About", className="nba", style={"fontSize":"1.3rem"}),
                    href="/apps/about",
                ),
                style={"display": "flex", "align-items": "baseline"}
            ),

        ],

        className="navbar",
        fluid=True,
        color="primary",
        sticky=True,
        dark=True
    )


    return navbar
