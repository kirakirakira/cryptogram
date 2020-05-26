import json
import re


class Dump:
    def __init__(self):
        self.tweets = dict({})
        self.clean_tweets = dict({})
        self.load_tweets()

    def load_tweets(self):
        f = open('trumpograms/trump.json')

        trump_dump = json.load(f)

        re.sub("[a-zA-Z]", "_", "abcdefghiject")

        for index, tweet in enumerate(trump_dump, start=1):
            self.tweets[index] = tweet['text']

        self.clean_tweets = {
            k: v for k, v in self.tweets.items() if not v.startswith('RT')}
        self.clean_tweets = {
            k: v for k, v in self.clean_tweets.items() if not v.startswith('https')}

        for index, tweet in self.clean_tweets.items():
            self.clean_tweets[index] = re.sub(
                r"http\S+", '', self.clean_tweets[index])
            self.clean_tweets[index] = re.sub(
                r"@\S+", '@_%&*#$%^', self.clean_tweets[index])

        f.close()

    def get_tweets(self):
        return self.clean_tweets

    def display_tweets(self):
        for key, value in self.clean_tweets.items():
            print(key)
            print(value)


if __name__ == '__main__':
    dump = Dump()
    dump.display_tweets()
