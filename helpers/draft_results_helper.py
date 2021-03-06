import requests
import pandas as pd


def create_df(records):
    temp_df = pd.DataFrame(dtype='object')

    for pick in records:
        temp_df = temp_df.append(pd.json_normalize(pick), ignore_index=True)

    temp_df = temp_df.set_index('pickNumber')

    temp_df = temp_df.rename(axis=1, mapper=lambda x: x.split('.')[-1])
    temp_df = temp_df.rename({'teamName': 'Team Name',
                            'displayName': 'Draft Pick',
                            'position': 'Position',
                            'feetAndInches': 'Ft',
                            'weightLbs': 'Wt',
                            'school': 'School',
                            'status': 'Status',
                            'country': 'Country'},
                           axis=1)

    return temp_df[['Draft Pick', 'Team Name', 'Position', 'Ft', 'Wt', 'School', 'Status', 'Country']]


def get_lottery_picks():

    url = "https://content-api-prod.nba.com/public/1/draft/2021/board"

    payload={}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.nba.com/',
        'Origin': 'https://www.nba.com',
        'DNT': '1',
        'Connection': 'keep-alive'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    lotto_df = pd.DataFrame(response.json())

    picks = lotto_df.loc['picks', 'results']

    first_round_picks = create_df(picks['firstRound'])
    second_round_picks = create_df(picks['secondRound'])


    return first_round_picks, second_round_picks

    # html_string = '''
    # <html>
    #   <link rel="stylesheet" type="text/css" href="lottery.css"/>
    #   <body>
    #     {table}
    #   </body>
    # </html
    # '''
    #
    # with open('picks.html', 'w') as f:
    #   f.write(html_string.format(table=lottery_df.to_html()))
