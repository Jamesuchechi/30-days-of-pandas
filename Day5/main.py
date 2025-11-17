import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['len'] = tweets['content'].str.len()
    return tweets[tweets['len'] > 15][['tweet_id']]
