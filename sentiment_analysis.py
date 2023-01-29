import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

def get_sentiment_score(selftext, title):
    # combine = ""
    if not selftext and not title:
        return 0
    elif not selftext:
        combine = title
    elif not title:
        combine = selftext
    else:
        combine = selftext + title
    return sia.polarity_scores(combine)['compound']





print(get_sentiment_score("I love tesla", "elon musk"))
print(get_sentiment_score("I hate tesla", "dumb elon musk"))
print(get_sentiment_score("tesla is not amazing", "buy it"))
print(get_sentiment_score("tesla is losing all of my money", "don't buy it"))

print(get_sentiment_score("Shout out to WSB, if I didn't see everyone mentioning TSLA puts I wouldn't have known to buy calls", ""))
print(get_sentiment_score("", "AMZN is a buy."))

