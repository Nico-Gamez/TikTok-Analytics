# Imports
from TikTokApi import TikTokApi as tiktok
import json
import pandas as pd
#Import data processing data
from helpers import process_results
#Import sys dependency to extract command line arguments
import sys

api = tiktok(use_test_endpoints=True)
trending = []


def get_data(hashtag):

    # Get data by hashtag
    with tiktok() as api:
        tag = api.hashtag(name = hashtag)

        #print(tag.info())

        for video in tag.videos():
            trending.append(video.as_dict)
            #print(video.as_dict)
        
        flattened_data = process_results(trending)

    ##Export data to json
    #with open('export.json', 'w') as f:
    #   json.dump(flattened_data, f)

    #Convert the preprocessed data to a dataframe
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('TikTok_data.csv', index=False)

#When run from command line make sure that we run the function main
if __name__ == '__main__':
    print(sys.argv[1])
    get_data(sys.argv[1])