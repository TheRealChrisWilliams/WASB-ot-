import tweepy
from scraper import tips_and_resources
import time
from decouple import config

# Your Twitter API credentials
consumer_key = config("YOUR_CONSUMER_KEY")
consumer_secret = config("YOUR_CONSUMER_SECRET")
access_token = config("YOUR_ACCESS_TOKEN")
access_token_secret = config("YOUR_ACCESS_TOKEN_SECRET")

# Create a Twitter client
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

for item in tips_and_resources:

    tweet_text = item["title"] + "\n" + item["link"] + "\n#gamedev #indiegames #gamingnews #gamingindustry #gamebot" + " #" + item['title'].split(" ", 1)[0].lower()

    response = client.create_tweet(text=tweet_text)
    print(response)
    time.sleep(20)
