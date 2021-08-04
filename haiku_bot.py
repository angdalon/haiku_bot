import tweepy
import random
import time
import datetime
from dotenv import dotenv_values
from tweepy.error import TweepError

if __name__ == '__main__':
    envVars = dotenv_values(".env")
    envKeys = list(envVars.values())

class Bot:
    def __init__(self, keys):
        self._consumer_key = keys[0]
        self._consumer_secret = keys[1]
        self._access_token = keys[2]
        self._access_secret = keys[3]

        try:
            auth = tweepy.OAuthHandler(self._consumer_key,
                                       self._consumer_secret)
            auth.set_access_token(self._access_token, self._access_secret)

            self.client = tweepy.API(auth)
            if not self.client.verify_credentials():
                raise tweepy.TweepError
        except tweepy.TweepError as e:
            print('ERROR : connection failed. Check your OAuth keys.')
        else:
            print('Connected as @{}, bot is running!'.format(self.client.me().screen_name))
            self.client_id = self.client.me().id

            def get_last_tweet(self):
                tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
                print(tweet.text)
        

        thedayis = datetime.datetime.today().weekday()
        if thedayis == 0:
            thepoemfile = "haiku_hu.txt"
            hashT = "#magyar #haiku"
        elif thedayis == 1:
            thepoemfile = "haiku_de.txt"
            hashT = "#deutsche #haiku"
        elif thedayis == 2:
            thepoemfile = "haiku_fr.txt"
            hashT = "#haiku #français"
        elif thedayis == 3:
            thepoemfile = "haiku_es.txt"
            hashT = "#haiku #español"
        elif thedayis == 4:
            thepoemfile = "haiku_se.txt"
            hashT = "#svenska #haiku"
        elif thedayis == 5:
            thepoemfile = "haiku_it.txt"
            hashT = "#haiku #italiano"
        elif thedayis == 6:
            thepoemfile = "haiku_jp.txt"
            hashT = "#俳句"

        def post_poem():
            with open(thepoemfile, "r", encoding='utf-8') as fh:
                alltext = fh.readlines()

            x = random.randrange(0, len(alltext)-4, 7)
            dailypoem = alltext[x:x+5]
            actualdailypoem = (dailypoem[0] + dailypoem[1] + dailypoem[2] + dailypoem[3] + dailypoem[4])
            
            try:
                self.client.update_status(actualdailypoem + hashT)
            except tweepy.TweepError as e:
                print(e)
                print("Trying again in 10 seconds.")
                time.sleep(10)
                post_poem()

        post_poem()
        print("Poem sent, exiting now!")

Bot(envKeys)