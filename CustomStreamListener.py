import tweepy
from login_twitter import login
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from mongodbconnect import save_data_mongo
import pymongo
from tweepy.utils import import_simplejson




CONSUMER_KEY = 'j3exsQjbu3Div4sFaBNudTi79'
CONSUMER_SECRET = 'mxmkRrxade4omPKhsCqIWOCgaZv38N0m2fpVN3txfPwhiY5h6h'
OAUTH_TOKEN = '47028803-PO6xteN2Q7nMnnO62ImDax869EStOCrqgO78aYNt5'
OAUTH_TOKEN_SECRET = 'gdlNcRgabLjSPw0cMS6gz4kYe8oN8v2ySkEjCKAvHApVG'
json = import_simplejson()




class StdOutListener(StreamListener):
    
    json = import_simplejson()
    
    def error():
        print "hello"
    
    def on_data(self,data):
        
	    SEED_DATA = json.loads(data)
	    save_data_mongo(SEED_DATA)
	    print SEED_DATA
	    return True
	    
if __name__== '__main__':
    
    l = StdOutListener()
    auth = login()
    twitter_api = tweepy.API(auth)
    stream = Stream(auth,l)
    stream.filter(track=['python','javascript','ruby'])

