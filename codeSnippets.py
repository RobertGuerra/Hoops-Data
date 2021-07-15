

# DATUM CONTIANS:
# 'displayName', 'logo', 'record', 'standingSummary', 'color', 'alternateColor'


# code for first place teams
# firstPlace = "first_place" if "1st" in datum['standingSummary'] else ''


# NOT QUITE RIGHT
# def get_team_roster():
#     data_access = allData['sports']
#     for leagues_access in data_access:
#         league_data = leagues_access['leagues']
#         #print(league_data)
#         for access_teams in league_data:
#             the_teams = access_teams['teams']
#             #print(the_teams)
#             for access_Individual_teams in the_teams:
#                 each_team = access_Individual_teams['team']
#                 #print(each_team)
#                 for team_roster_links in each_team['links']:
#                     team_rosters = team_roster_links
#                     (print(team_rosters))


#  getting info directly from json file and traversing through it
# with open('teams.json', 'r') as json_file:
#     allData = json.load(json_file)
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