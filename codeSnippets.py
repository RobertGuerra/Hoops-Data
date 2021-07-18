
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


