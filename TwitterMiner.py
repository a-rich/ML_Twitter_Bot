from Miner import Miner
from TweetFeed import TweetFeed
import threading
import time
import pprint as p

terms = ['Bay Area','bay area','BAY AREA','Bay area','bay Area']
coordinates = [36.8,-122.52,38,-121.75]

tf1 = TweetFeed('/Users/aweeeezy/bin/python/ML_Twitter_Bot/TwitterTokens.txt',20)
#tf2 = TweetFeed('/Users/aweeeezy/bin/python/ML_Twitter_Bot/TwitterTokens.txt',20)
print "\n********************************************************************\n"
wordStreamThread = threading.Thread(target=tf1.filterKeywords, args=([terms]))
#locStreamThread = threading.Thread(target=tf2.filterLocations, args=([coordinates]))
wordStreamThread.daemon = True
#locStreamThread.daemon = True
wordStreamThread.start()
#locStreamThread.start()
#wordStreamThread.join()
#locStreamThread.join()
time.sleep(240)
print "*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*"
print len(tf1.tweets), "tweets with 'Bay Area' and geo tags in the area!"
#print len(tf2.tweets), "tweets with geo tags & 'Bay Area' in the text logged!"

