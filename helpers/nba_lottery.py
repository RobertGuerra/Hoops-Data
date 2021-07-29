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

print("before flatten...")
print(lottery_data)

def flatten(current, key, result):
  if isinstance(current, dict):
    for k in current:
      new_key = "{0}.{1}".format(key, k) if len(key) > 0 else k
      flatten(current[k], new_key, result)
    else:
      result[key] = current
    return result


result = flatten(lottery_data, '', {})
print("\n\nafter flatten...\n")
print(result)



