import pandas as pd

def filter_json(res):
    ser = pd.Series(res)


    # WE WANT displayName, color, alternateColor, standingSummary, logo, and record ovr
    raw_ser = ser[["displayName", "logos", "record", "standingSummary", "color", "alternateColor", "links"]]

    logo = raw_ser["logos"][0]["href"]
    record_ovr = raw_ser["record"]["items"][0]["summary"]
    team_link = raw_ser["links"][1]["href"]

    refined_ser = raw_ser

    refined_ser["team-link"] = team_link
    refined_ser["logos"] = logo
    refined_ser["record"] = record_ovr
    refined_ser.rename({"logos": "logo"}, inplace=True)

    return refined_ser.to_dict()