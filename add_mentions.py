#!/usr/bin/env python3

import json
from tqdm.auto import tqdm

with open("pivotonline_tweets_2020_twarc.geojson") as f:
    tweets = json.load(f)

for i, tweet in enumerate(tqdm(tweets["features"])):
    for other_tweet in tweets["features"]:
        screen_name = other_tweet["properties"]["screen_name"]
        if screen_name == tweet["properties"]["screen_name"]: # self mention
            continue
        if "@" + screen_name in tweet["properties"]["text"]:
            if "mentions" not in tweets["features"][i]["properties"]:
                tweets["features"][i]["properties"]["mentions"] = []
            if screen_name not in tweets["features"][i]["properties"]["mentions"]:
                tweets["features"][i]["properties"]["mentions"].append(screen_name)

print(json.dumps(tweets,indent=2))