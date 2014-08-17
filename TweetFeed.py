import sys
import json
from tweepy import api
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

class TweetFeed(StreamListener):
    def __init__(self, tokenFile, limit):
	lines = open(tokenFile,'r').read().split('\n')
	cKey = lines[0]
	cSecret = lines[1]
	aToken = lines[2]
	aSecret = lines[3]
	self.auth = OAuthHandler(cKey,cSecret)
	self.auth.set_access_token(aToken,aSecret)
	self.filterType = ''
	self.tweets = {}
	self.tweetCount = 0
	self.streamLimit = limit

    def on_data(self, data):
	tweet = json.loads(data)
	if self.filterType == 'loc':
	    print "it's a location post..."
	    if self.refineText(tweet) == True:
		print "\twas able to refine post using text"
		self.tweets[tweet['id_str']] = tweet
		self.tweetCount += 1
	elif self.filterType == 'keyword':
	    print "it's a text post..."
	    if self.refineGeo(tweet) == True:
		print "\twas able to refine post using coordinates"
		self.tweets[tweet['id_str']] = tweet
		self.tweetCount += 1
	if self.tweetCount < self.streamLimit:
	    return True
	else:
	    return False

    def filterKeywords(self, keyWords):
	self.filterType = 'keyword'
	self.keyWords = keyWords
	twitterStream = Stream(self.auth,self)
	twitterStream.filter(track=keyWords)

    def filterLocations(self, coordinates):
	self.filterType = 'loc'
	self.coordinates = coordinates
	twitterStream = Stream(self.auth,self)
	twitterStream.filter(locations=coordinates)

    def refineGeo(self,tweet):
	if tweet['geo'] != None:
	    print "geo isn't null"
	    if tweet['geo']['coordinates'] != None:
		print "\tcoordinates aren't null"
		lat = tweet['geo']['coordinates'][0]
		longi = tweet['geo']['coordinates'][1]
		if -122.52 >= lat <= -121.75 and 36.8 >= longi <= 38:
		    print "Found a local tweet!"
		    return True
	else:
	    print "eh, done with refineGeo ***"
	    return False

    def refineText(self,tweet):
	text = tweet['text']
	for word in self.keyWords:
	    if word in text:
		print "Found relevant tweet!"
		return True
	print "eh, done with refineText ***"
	return False

