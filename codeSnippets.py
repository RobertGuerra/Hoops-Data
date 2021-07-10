

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


# THIS WORKS!!  ONLY ROSTER LINKS
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
#                 print(each_team['links'][1]['href'])
