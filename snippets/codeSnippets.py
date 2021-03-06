
# DATUM CONTIANS:
# 'displayName', 'logo', 'record', 'standingSummary', 'color', 'alternateColor'


# code for first place teams
# firstPlace = "first_place" if "1st" in datum['standingSummary'] else ''

# code for team cards
# color="#" + team_color,
# textShadow="-0.4px 0.6px #" + alt_color,



# getting info directly from json file and traversing through it
# with open('teams.json', 'r') as json_file:
#
# allData = json.load(json_file)
#
# def get_team_roster():
#     team_roster_links = []
#     data_access = allData['sports']
#     for leagues_access in data_access:
#         league_data = leagues_access['leagues']
#         #print(league_data)
#         for access_teams in league_data:
#             the_teams = access_teams['teams']
#             #print(the_teams)
#             for access_Individual_teams in the_teams:
#                 each_team = access_Individual_teams['team']
#                 team_roster_links.append(each_team['links'][1]['href'])
#     return team_roster_links
#
# teamRosters = get_team_roster()




# meta tags for small phone devices (uploaded to github)
# app start
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
#                 meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0, maximum-scale-1.2, minimum-scale=0.5'}])



# manual way of centering cards
# style={
            #     "width": "25%",
            #     "margin-left": "475px",
            #     "margin-top":"10px",
            #     "margin-bottom":"10px",
            #     "verticalAlign":"middle",
            #     "color":"#000000"
            # }

# dbc.CardFooter(
            #     [
            #         html.Div(
            #             [
            #                 # html.P(f"Season Record: {record}"),
            #                 # html.P(f"Standing: {summary}",
            #                 #        className=numberOne)
            #                 html.A(html.Button('Team Roster'),
            #                        href='https://github.com/czbiohub/singlecell-dash/issues/new'
            #         ),
            #             ],
            #         ),
            #     ],
            #
            #     style=dict(
            #         display="flex",
            #         backgroundColor='#' + team_color,
            #         justifyContent="center"
            #     )
            # )


# old code for drop down menu
# .dropdown {
#     padding: 15px;
#     width: 295px;
#     display: flex;
#     color: black !important;
# }
#
# .dropdown-div {
#     justify-content: center;
# }


# new code for the drop down menu

# https://stackoverflow.com/questions/56402207/style-dash-components-with-dark-theme-bootstrap-css
#
# .Select-control {
#     background-color: #222 !important;
# }
#
# .Select.is-focused > .Select-control {
#     background-color: #222;
# }
#
# #school-input {
#     color: white;
# }
#
# .Select-value-label {
#     color: white;
# }
#
# .Select--single > .Select-control .Select-value, .Select-placeholder {
#     border: 1px solid grey;
#     border-radius: 4px;
# }
#
# .VirtualizedSelectOption {
#     background-color: #222;
#     color: white;
#  }
#
# .VirtualizedSelectFocusedOption {
#     background-color: #222;
#     opacity: .7;
# }
#
# .Select.is-focused:not(.is-open) > .Select-control {
#     background-color: #222;
#     border-color: var(--primary);
#     box-shadow: none;
# }



# SECTION: DCC DROPDOWN IMPLEMENTATION
# dcc.Dropdown(
#     id="team-list",
#     options=[
#         {"label": i, "value": i}
#         for i in sorted(
#             ["All Teams", "Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"])
#
#     ],
#
#     className="dropdown",
# )


# code to flatten a dictionary
# def flatten(current, key, result):
#   if isinstance(current, dict):
#     for k in current:
#       new_key = "{0}.{1}".format(key, k) if len(key) > 0 else k
#       flatten(current[k], new_key, result)
#     else:
#       result[key] = current
#     return result
#
#
# result = flatten(lottery_data, '', {})
# print("\n\nafter flatten...\n")
# print(result)


#   2 different options for inserting an image into a dbc card
# dbc.CardImgOverlay(
                        #     children=[
                        #         html.Img(
                        #             src="../assets/chi_op.jpg",
                        #             style={
                        #                 "z-index": "0",
                        #                 "position": "absolute",
                        #                 "padding-bottom": "0px",
                        #                 "padding-top":"67px",
                        #                 "bottom":"-2px",
                        #                 "left":"0px",
                        #                 "width": "99vw",
                        #                 "height": "30vh",
                        #                 "object-fit": "cover",
                        #                 "mix-blend-mode":"hard-light"
                        #             }
                        #         )
                        #     ],
                        # ),

# dbc.CardImg(
                        #     src="../assets/chi_op.png", top=False, bottom=True,
                        #     style={
                        #         "background-image": 'url("../assets/chi_op.png")',
                        #         "background-repeat": "no-repeat",
                        #         "display": "block",
                        #         "width": "99vw",
                        #         "height": "25vh",
                        #         "object-fit": "cover",
                        #         "z-index": "0"
                        #     },
                        # ),
                        
# working navbar
# nav = dbc.NavbarSimple(
#         children=[
#
#             html.Img(
#                 src="https://s3.amazonaws.com/file.imleagues/Images/Teams/Uploaded/201801/201812316271650f5a72e9de44767031d56a47aca3fcadf.png",
#                 style={
#                     "height": "10%",
#                     "width": "10%",
#                     "display": "inline-bock",
#                 }
#             ),
#
#             html.Div(
#                 dbc.NavLink(
#                     html.H1("NBA"),
#                     href="https://www.nba.com/",
#                     target="blank",
#                     className="nba",
#                     style={"padding-right": "30%", "overflow": "hidden", "display": "inline-block"}
#
#                 ),
#             ),
#
#             html.H1(
#                 "TITLE HERE",
#                 style={"padding-left":"200px"}
#             ),
#
#
#             dbc.DropdownMenu(
#                 [
#                     dbc.DropdownMenuItem(i, id=i)
#                     for i in sorted(
#                         ["All Teams", "Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"]
#                     )
#                 ],
#                 nav=True,
#                 label="Select Division",
#                 id="team-list",
#                 in_navbar=True,
#                 className="dropdown",
#                 style={"padding-left":"300px"}
#             )
#
#         ],
#
#         className="navbar",
#         color="primary",
#         sticky=True,
#         dark=True
#     )
