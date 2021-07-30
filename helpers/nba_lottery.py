import requests
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


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

  pd.json_normalize(picks['firstRound'][0])
  # new_home = lotto_df['results'][6]['firstRound'][0]['team']

  pd.set_option('colheader_justify', 'center')

  df = pd.DataFrame(dtype='object')

  for pick in picks['firstRound']:
      df = df.append(pd.json_normalize(pick), ignore_index=True)

  df = df.set_index('pickNumber')

  df = df.rename(axis=1, mapper=lambda x: x.split('.')[-1])

  lottery_df = df[['teamName','displayName','position','feetAndInches','weightLbs','school','status','country']]

  html_string = '''
  <html>
    <link rel="stylesheet" type="text/css" href="lottery.css"/>
    <body>
      {table}
    </body>
  </html
  '''

  with open('picks.html', 'w') as f:
    f.write(html_string.format(table=lottery_df.to_html()))


get_lottery_picks()