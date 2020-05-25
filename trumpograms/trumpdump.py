import json
import re

f = open('trump.json')

trump_dump = json.load(f)

tweets = dict({})
re.sub("[a-zA-Z]", "_", "abcdefghiject")

for index, tweet in enumerate(trump_dump, start=1):
    tweets[index] = tweet['text']
    # tweets[index] = re.sub(r"http\S+", '', tweets[index])
    # print(index)
    # print(tweets[index])
    # print("--"*8)

# keys_to_delete = []

# for key, value in tweets.items():
#     if value.startswith('RT'):
#         keys_to_delete.append(key)

# for key in keys_to_delete:
#     del tweets[key]

new_tweets = { k:v for k, v in tweets.items() if not v.startswith('RT')}
new_tweets = { k:v for k, v in new_tweets.items() if not v.startswith('https')}

for key, value in new_tweets.items():
    print(key)
    print(value)

f.close()
