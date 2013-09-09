from BeautifulSoup import BeautifulSoup
from django.conf import settings
from ifwm.home.helpClasses import getTime, getMD5Str
from ifwm.home.models import *
import urllib2
import urlparse

def addImagesFromPage(page):
	pageurl = page.url.url
	pagehost = urlparse.urlparse(pageurl).netloc
	uopen = urllib2.urlopen(pageurl, data, 3000)
	#check size
	ssize = result.headers['content-length']
	size = int(ssize)
	page.url.date =getTime()
	#ban big pages
	#and not web pages
	if size > settings.MAX_FETCH_PAGE_SIZE or not result.headers['content-type'] == 'text/html':
		page.url.status = 4
		page.url.save()
		return []
	#get urls
	parser = BeautifulSoup(uopen.read())
	imgurls = []
	for img in setsoup.find_all('img'):
		imgurls.append(img.get('src'))
	parser = None
	#find urls to this domain + subdomains
	finurls = set()
	for img in imgurls:
		o = urlparse(img)
		curl = None
		if o.netloc=='':
			curl = urlparse.urljoin(pageurl, o.path)
		elif o.netloc == pagehost:
			curl = img
		elif o.netloc.endswith('.'+pagehost):
			curl = img
		if not curl:
			continue
		o=None
		
	imgurls=None
	
	return finurls