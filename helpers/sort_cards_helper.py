import pandas as pd


def sort_cards(json_data, division):

    # Create a temporary DataFrame
    temp_df = pd.DataFrame.from_records(json_data)

    # Take the standingSummary column and apply a function that parses the Division of every team
    temp_df["Division"] = temp_df["standingSummary"].apply(lambda summary: summary.split(' ')[2])

    # Filter through original json data and return only those that match the division passed in from callback
    temp_df = temp_df[temp_df.loc[:, "Division"] == division]

    # Take the standingSummary column and apply a function that parses the Rank of every team
    temp_df["Rank"] = temp_df["standingSummary"].apply(lambda summary: int(summary[0]))

    # Sort the DataFrame by the Rank and return it to its original form DataFrame -> Record Array
    # (NOTE: Record Array is a List of dictionaries: [{k1: v1}, {k2: v2}, ... , {kN: vN}]
    temp_df = temp_df.sort_values(by="Rank").to_records()

    return temp_df

