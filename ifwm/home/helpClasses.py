import json
from django.core.paginator import Page

#image[] -> {}[]
def imgArrToDD(images):
	cnt = len(images)
	retval = [None]* cnt
	for i in range(0,cnt):
		retval[i] = imgToDict(images(i))
	return retval
def imgToDict(image):
	return {
		'url':image.url.url,
		'status': image.url.status,
		'imageid': image.pk,
		'preview': image.has_s,
	}
def pageToDict(page):
	return {
		'pageid' : page.pk,
		'status': page.url.status,
		'ready' : page.images_ready,
		'total' : page.images_total,
		'url' : page.url.url,
	}

class Error(object):
	caption = ''
	full_text = ''
	def __init__(self, caption, full_text):
		self.caption = caption
		self.full_text = full_text
class ProgressInfo(object):
	page = None
	timestamp = 0
	images = None
	def __init__(self, page, timestamp, images):
		self.page = page
		self.timestamp = timestamp
		self.images = list(images)
	def getJson(self):
		progress = {
			'result' : 'ok',
			'page': pageToDict(self.page), 
			'timestamp': self.timestamp,
			'images': imgArrToDD(self.images)
		}
		return json.dumps(progress)
