class Error(object):
	caption = ''
	full_text = ''
	def __init__(self, caption, full_text):
		self.caption = caption
		self.full_text = full_text
class ProgressInfo(object):
	page = None
	timestamp = 0
	status = 0
	images = None
	def __init__(self, page, timestamp, status, images):
		self.page = page
		self.timestamp = timestamp
		self.status = status
		self.images = images
	def getJson(self):
		import json		
		progress = {
				'pageid': self.page.pk,
				'timestamp': self.timestamp,
				'status': self.page.url.status,
				'images': list(self.images)
		}
		return json.dumps(progress)