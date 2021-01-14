import tweepy
import textblob
from operator import itemgetter
#from wordcloud import WordCloud
import preprocessor as p
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweepy import OAuthHandler
import pandas as pd
import nltk
nltk.download('vader_lexicon')

def twitterRating(searchItem):
    

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    tweetText = []
    def print_tweets(tweets):
        for tweet in tweets:
            #tweetStr = tweet.entities['user_mentions'][0]['screen_name']
            #print(f'{tweet.text}:', end=' ')
            tweetText.append(tweet.text)

    tweets = api.search(q= searchItem, count=50, lang = 'en')
    print_tweets(tweets)
    #tweetText
    tidyTweetText = []
    p.set_options(p.OPT.URL, p.OPT.RESERVED, p.OPT.MENTION)
    for tweet in tweetText:
        tidyTweetText.append(p.clean(tweet))
    #tidyTweetText
    tweetDict = {'tweets': tidyTweetText}
    df = pd.DataFrame(tweetDict)
    #df
    sid = SentimentIntensityAnalyzer()
    df['scores'] = df['tweets'].apply(lambda tweet: sid.polarity_scores(tweet))
    df['compound']  = df['scores'].apply(lambda score_dict: score_dict['compound'])
    df['comp_score'] = df['compound'].apply(lambda c: 'pos' if c >0 else 'neg')


    """
    pos = 0
    total = len(df.index)
    for ind in df.index:
        if df['comp_score'][ind] == 'pos':
            pos = pos + 1

    (pos/total)*100
    """

    totalReal = 0
    pos = 0
    for ind in df.index:
        if df['compound'][ind] != 0:
            totalReal = totalReal + 1
        if df['comp_score'][ind] == 'pos':
            pos = pos + 1
    #totalReal
    #total
    if totalReal == 0:
        return 0
    rating = (pos/totalReal)*100
    rating = round(rating,2)
    return rating #This is the real positivity after removing neutral statements
