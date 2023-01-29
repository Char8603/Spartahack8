# https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c
import requests
from requests.auth import HTTPBasicAuth
import pandas
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from nltk import tokenize

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

def retreive_many_posts(headers, stock, params={'limit': '100'}):
    dataframe = pandas.DataFrame()

    for i in range(10):
        result = requests.get("https://oauth.reddit.com/r/wallstreetbets/search/?q=" + stock + "&restrict_sr=1&sr_nsfw=&sort=new",
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

def get_posts_from_day(data):
    results = []
    day = data.iloc[0]["created_utc"][0:10]

    for post in data.iloc:
        #if post["created_utc"][0:10] == day:
        #print(post["created_utc"][0:10])
        results.append(post)
    return results

def get_sentiment_scores(data):
    scores = []

    upvotes = 0

    for post in data:
        upvotes += int(post["ups"])
        sentences = [post["title"] + post["selftext"]]

        values = []

        for sentence in sentences:
            sid = SentimentIntensityAnalyzer()
            #print(sentence)
            ss = sid.polarity_scores(sentence)
            for k in sorted(ss):
                #print('{0}: {1}, '.format(k, ss[k]), end='')
                values.append(float(ss[k]))
            #print()
        values.append(int(post["ups"]))
        values.append(float(post["upvote_ratio"]))
        scores.append(values)

    return (scores, upvotes)     

def process_scores(scores, upvotes):
    results = [0, 0, 0]
    for score in scores:
        up_ratio = score[4] / upvotes
        results[0] += up_ratio * score[1] * score[-1]
        results[1] += up_ratio * score[2] * score[-1]
        results[2] += up_ratio * score[3] * score[-1]
    return results


if __name__ == "__main__":
    stock = "GME"
    headers = initialize_connection()
    #posts = retreive_posts(headers)
    #display_titles(posts)  
    #data = format_data(posts)
    data = retreive_many_posts(headers, stock)
    posts = get_posts_from_day(data)
    scores, upvotes = get_sentiment_scores(posts)
    results = process_scores(scores, upvotes)
    sum_res = sum(results)
    for i in range(len(results)):
        results[i] = results[i] / sum_res * 100

    print(results)
    
    