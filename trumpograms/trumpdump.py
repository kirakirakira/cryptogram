import json
import re

f = open('trump.json')

trump_dump = json.load(f)

tweets = dict({})
re.sub("[a-zA-Z]", "_", "abcdefghiject")

for index, tweet in enumerate(trump_dump, start=1):
    # tweets[index] = "     ".join(tweet['text'].split())
    # tweets[index] = re.sub("[a-zA-Z]", "_ ", tweets[index])
    tweets[index] = tweet['text']
    tweets[index] = re.sub(r"http\S+", '', tweets[index])
    print(index)
    print(tweets[index])
    print("--"*8)


f.close()
