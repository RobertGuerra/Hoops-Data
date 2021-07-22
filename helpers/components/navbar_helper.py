import dash_html_components as html
import dash_bootstrap_components as dbc


def Navbar():

    nav = dbc.Nav(
        [
            dbc.Navbar(
                children=[
                    dbc.NavItem(
                        dbc.NavLink(
                            html.H1("NBA"),
                            href="https://www.nba.com/",
                            target="blank",
                            className="nba",
                        )
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            html.H1(
                                "HOOPS"
                            ),
                            style={"color": "white"}
                        )
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            dbc.DropdownMenu(
                                [
                                    dbc.DropdownMenuItem(i, id=i)
                                    for i in sorted(
                                    ["All Teams", "Atlantic", "Southeast", "Central",
                                     "Northwest", "Pacific", "Southwest"]
                                )
                                ],

                                nav=True,
                                label="All Teams",
                                id="team-list",
                                in_navbar=True,
                                className="dropdown",
                            )
                        )
                    )],sticky=True, className="navbar"
            )

            # dbc.NavItem(
            #     dbc.NavLink(
            #         html.H1("NBA"),
            #         href="https://www.nba.com/",
            #         target="blank",
            #         className="nba",
            #     )
            # ),
            # dbc.NavItem(
            #     dbc.NavLink(
            #         html.H1(
            #             "HOOPS"
            #         ),
            #         style={"color":"white"}
            #     )
            # ),
            # dbc.NavItem(
            #     dbc.NavLink(
            #         dbc.DropdownMenu(
            #             [
            #                 dbc.DropdownMenuItem(i, id=i)
            #                 for i in sorted(
            #                     ["All Teams", "Atlantic", "Southeast", "Central",
            #                      "Northwest", "Pacific", "Southwest"]
            #                 )
            #             ],
            #
            #             nav=True,
            #             label="All Teams",
            #             id="team-list",
            #             in_navbar=True,
            #             className="dropdown",
            #         )
            #     )
            # )
        ],

        fill=True,
        justified=True,
    )

    return nav

