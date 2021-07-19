import requests
import json

from helpers.filter_json_helper import filter_json

### INITIALIZE START ###

json_data = []

ABBR = ["ATL", "BOS","CHA","CHI","CLE","DAL", "DEN","DET",
        "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA",
        "MIL", "MIN", "NO", "NYK", "BKN", "OKC", "ORL", "PHI",
        "PHO", "POR", "SAC", "SAS", "TOR", "UTH", "WAS"]

BASE_URL = 'http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/'

for team in ABBR:
    request = requests.get(BASE_URL + f'{team}')
    json_response = json.loads(request.content)['team']

    # filter_json: helper function from filter_json_helper
    json_data.append(filter_json(json_response))
