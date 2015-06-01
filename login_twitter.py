import tweepy


CONSUMER_KEY = 'j3exsQjbu3Div4sFaBNudTi79'
CONSUMER_SECRET= 'mxmkRrxade4omPKhsCqIWOCgaZv38N0m2fpVN3txfPwhiY5h6h'
OAUTH_TOKEN = '47028803-PO6xteN2Q7nMnnO62ImDax869EStOCrqgO78aYNt5'
OAUTH_TOKEN_SECRET = 'gdlNcRgabLjSPw0cMS6gz4kYe8oN8v2ySkEjCKAvHApVG'


def login(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,
						auth_token=OAUTH_TOKEN, auth_token_sec=OAUTH_TOKEN_SECRET):

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(auth_token, auth_token_sec)
	return auth

	

if __name__== '__main__':

	login(CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)