import json
import time
from hashlib import md5
from ifwm.settings import DBG_OUT_LEVEL

def dbgOut(msg, lvl):
    if lvl >= DBG_OUT_LEVEL:
        print msg


def getMD5Str(inputStr):
    hasher = md5()
    hasher.update(inputStr)
    return hasher.hexdigest()


def getTime():
    return int(time.time())


#image[] -> {}[]
def imgArrToDD(images):
    cnt = len(images)
    retval = [None] * cnt
    for i in xrange(0, cnt):
        retval[i] = imgToDict(images[i])
    return retval


def imgToDict(image):
    return {
        'url': image.url.url,
        'status': image.url.status,
        'imageid': image.pk,
        'preview': image.has_s,
        'ext':  image.ext
    }


def pageToDict(page):
    return {
        'pageid':   page.pk,
        'status':   page.url.status,
        'ready':    page.images_ready,
        'total':    page.images_total,
        'url':      page.url.url,
    }


class Error(object):
    caption = ''
    full_text = ''

    def __init__(self, caption, full_text):
        self.caption = caption
        self.full_text = full_text


class ProgressInfo(object):
    _page = None
    _timestamp = 0
    _images = None

    def __init__(self, page, timestamp, images):
        self._page = pageToDict(page)
        self._timestamp = timestamp
        self._images = imgArrToDD(images)

    def getJson(self):
        progress = {
            'result': 'ok',
            'page': self._page,
            'timestamp': self._timestamp,
            'images': self._images
        }
        return json.dumps(progress)
