import json
import re

f = open('trump.json')

trump_dump = json.load(f)

tweets = dict({})
re.sub("[a-zA-Z]", "_", "abcdefghiject")

for index, tweet in enumerate(trump_dump, start=1):
    tweets[index] = tweet['text']

new_tweets = { k:v for k, v in tweets.items() if not v.startswith('RT')}
new_tweets = { k:v for k, v in new_tweets.items() if not v.startswith('https')}

for index, tweet in new_tweets.items():
    new_tweets[index] = re.sub(r"http\S+", '', new_tweets[index])
    new_tweets[index] = re.sub(r"@\S+", '@_%&*#$%^', new_tweets[index])

for key, value in new_tweets.items():
    print(key)
    print(value)

f.close()
