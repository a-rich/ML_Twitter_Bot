import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time

class Miner():
    def __init__(self):
	cj = CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	opener.addheaders = [('User-agent','Mozilla/5.0')]

    def source(page):
	try:
	    source = opener.open(page).read()
	    return source
	except Exception, e:
	    print str(e)

    def titles(source):
	titles = re.findall(r'<title>(.*?)</title>',sourceCode)
	return titles

    def links(source):
	link = re.findall(r'<link>(.*?)</link>',sourceCode)
	return link

    def text(source):
	text = re.findall(r'<p>(.*?)</p>',sourceCode)
	return text
