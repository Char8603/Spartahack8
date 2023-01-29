# https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c
import requests
from requests.auth import HTTPBasicAuth
import pandas
from datetime import datetime

def initialize_connection():
    auth = HTTPBasicAuth("tIYdIWoHf7b4oA_Y7h8cEA", "PYqCErcIFK4i8OA0deIYCnklSUB86g")

    data = {"grant_type": "password",
            "username": "Spartahack8-Stocky",
            "password": "Spartahack8-CNAB"}

    headers = {"User-Agent": "Stocky"}

    request = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)

    TOKEN = request.json()["access_token"]

    headers = {**headers, **{"Authorization": f"bearer {TOKEN}"}}

    requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)

    return headers

def retreive_posts(headers, params={'limit': '100'}):
    request = requests.get("https://oauth.reddit.com/r/wallstreetbets/new", headers=headers, params=params)

    return request.json()

def retreive_many_posts(headers, params={'limit': '100'}):
    dataframe = pandas.DataFrame()

    for i in range(10):
        result = requests.get("https://oauth.reddit.com/r/wallstreetbets/new",
                                headers=headers,
                                params=params)
        
        data = format_data(result.json())
        
        if len(data) > 0:
            params["after"] = data.iloc[len(data)-1]["fullname"]
            dataframe = pandas.concat([dataframe, data])
    
    return dataframe

def display_titles(posts):
    for post in posts["data"]["children"]:
        print(post["data"]["title"])

def format_data(posts):
    dataframe = pandas.DataFrame()

    for post in posts["data"]["children"]:
        dataframe = pandas.concat([dataframe, pandas.Series({
            "kind": post["kind"],
            "id": post["data"]["id"],
            "fullname": post["kind"] + '_' + post["data"]["id"],
            "subreddit": post["data"]["subreddit"],
            "created_utc": datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%dT%H:%M:%SZ'),
            "title": post["data"]["title"],
            "selftext": post["data"]["selftext"],
            "upvote_ratio": post["data"]["upvote_ratio"],
            "ups": post["data"]["ups"],
            "downs": post["data"]["downs"],
            "score": post["data"]["score"]
        }).to_frame().T], ignore_index=True)

    #print(dataframe)
    return dataframe

if __name__ == "__main__":
    headers = initialize_connection()
    posts = retreive_posts(headers)
    #display_titles(posts)  
    #data = format_data(posts)
    data = retreive_many_posts(headers)
    print(len(data))