import dash_html_components as html
import dash_bootstrap_components as dbc


def Navbar():
    nav = dbc.NavbarSimple(
        children=[
            html.H1(
                "TITLE HERE"
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
                className="dropdown"
            )

        ],

        className="navbar",
        brand="NBA",
        brand_href = "https://www.nba.com/",
        brand_external_link="https://www.nba.com/",
        color="primary",
        sticky=True,
        dark=True
    )

    return nav

