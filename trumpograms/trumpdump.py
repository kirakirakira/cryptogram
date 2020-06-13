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

        # Load tweets into self.tweets dictionary and slice them so they are 30 characters or less
        for index, tweet in enumerate(trump_dump, start=1):
            self.tweets[index] = tweet['text'][:30]

        # Remove tweets that start with RT (retweet) or start with a link (https)
        self.clean_tweets = {
            k: v for k, v in self.tweets.items() if not v.startswith('RT')}
        self.clean_tweets = {
            k: v for k, v in self.clean_tweets.items() if not v.startswith('https')}

        # Remove links and remove @ mentions
        for index, tweet in self.clean_tweets.items():
            self.clean_tweets[index] = re.sub(
                r"http\S+", '', self.clean_tweets[index])
            self.clean_tweets[index] = re.sub(
                r"@\S+", '@_%&*#$%^', self.clean_tweets[index])

        f.close()

    def get_tweets(self):
        return list(self.clean_tweets.values())

    def display_tweets(self):
        for key, value in self.clean_tweets.items():
            print(key)
            print(value)


if __name__ == '__main__':
    dump = Dump()
    dump.display_tweets()
