import requests
import json
import pandas as pd
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

response = requests.get(url, headers=headers)

lottery_data = response.json()

lotto_df = pd.DataFrame(lottery_data)

#new_home = lotto_df['results'][6]['firstRound']
new_home = 

print(pd.DataFrame.from_records(new_home).columns)



