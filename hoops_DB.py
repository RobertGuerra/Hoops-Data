import pandas as pd


from card.init_data import json_data

# trying to save to database
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:@localhost/hoops_data")

data = [datum for datum in json_data]
df = pd.DataFrame.from_records(data)
temp_df = pd.DataFrame.from_records(data)

df = df.loc[:,["displayName","logo","standingSummary","color","alternateColor","team-link","record_ovr"]]

#df.to_sql(con=my_conn,name='teams',if_exists='replace',index=False)

bn = pd.DataFrame(temp_df.record.tolist())['items'][0]

new_df = pd.DataFrame.from_records(bn).head()

print(temp_df['record'])
print("break\n\n")
print(new_df)