from BeautifulSoup import BeautifulSoup
from django.conf import settings
from ifwm.home.helpClasses import getTime, getMD5Str
from ifwm.home.models import *
from time import sleep
import re
import os.path
import urllib2
import urlparse

def parseIntOrZero(srting):
    try:
        return int(ssize)
    except:
        return 0


def copyStream(readStream, writeStream, count):
    downloaded = 0
    bufferSize = 16384
    try:
        while (downloaded<count):
            writeBuf = readStream.read(bufferSize)
            if not writeBuf:
                break
            downloaded += len(writeBuf)
            writeStream.write(writeBuf)
    finally:
        readStream.close()
        writeStream.close()


def fetUrl(img, savedir, maxsize=-1):
    try:
        url = img.url
        url.status = 1
        imageResponse = urllib2.urlopen(url.url, timeout=3000)
        #region check size
        ssize = imageResponse.headers['content-length']
        parseIntOrZero(ssize)
        url.date = getTime()
        contenttype = imageResponse.headers['content-type']
        if (
            size > settings.MAX_FETCH_IMAGE_SIZE or (
                not contenttype
            ) or (
                not contenttype.startswith('image/')
            )
        ):
            url.status=4
            url.save()
            return
        #extension
        if img.ext:
            ext = img.ext
        else:
            ext = re.search(
                'image/(\w+)',
                contenttype
            ).group(0)
        saveFileName = path.join(savedir, str(url.id)+'.'+ext)
        writeStream = open(saveFileName, 'wb')
        if size == 0:
            max_dwnld = settings.MAX_FETCH_IMAGE_SIZE
        else:
            max_dwnld = size
        try:
            copyStream(imageResponse, writeStream, max_dwnld)
        except Exception, e:
            os.remove(saveFileName)
            raise e
        url.status = 2
    except:
        url.status = 3
    url.save()


def findImageUrlsOnPage(page_str):
    parser = BeautifulSoup(page_str)
    imgurls = []
    for img in setsoup.find_all('img'):
        imgurls.append(
            img.get('src')
        )
    del parser
    return imgurls


def filterDomainImages(imgurls, pagehost):
    finurls = {}
    for img in imgurls:
        o = urlparse(img)
        if o.netloc == '':
            curl = urlparse.urljoin(
                pageurl,
                o.path
            )
        elif o.netloc == pagehost:
            curl = img
        elif o.netloc.endswith(
            '.' + pagehost
        ):
            curl = img
        del o
        if not curl:
            continue
        hash = getMD5Str(curl)
        #distinct
        if finurls[hash]:
            continue
        finurls[hash] = curl
        del curl
    del imgurls
    return finurls


#find queued images and add to DB
#return their urls
def addImagesFromPage(page):
    pageurl = page.url.url
    pagehost = urlparse.urlparse(pageurl).netloc
    uopen = urllib2.urlopen(
        pageurl,
        timeout=3000
    )
    returls = {}
    #check size
    #ban big pages and not web pages
    ssize = result.headers['content-length']
    parseIntOrZero(ssize)
    page.url.date = getTime()
    if size > settings.MAX_FETCH_PAGE_SIZE or (
        not result.headers['content-type'].startswith('text/')
    ):
        page.url.status = 4
        page.url.save()
        return returls
    #get urls
    imgurls = findImageUrlsOnPage(
        result.read()
    )
    del result
    if not imgurls:
        return retuls
    #find urls to this domain + subdomains
    goodurls = filterDomainImages(
        imgurls,
        pagehost
    )
    del imgurls
    if not finurls:
        return retuls
    #remove all !error queued
    #remove existing urls those don't need to be fetched
    #update
    hashes = goodurls.keys()
    images = Images.objects.filter(
        url__urlhash__in=hashes
    )
    images.prefetch_related('url')
    existing_urls_list = list(images)
    del images
    del hashes
    update_status = []
    for img in existing_urls_list:
        if (img.url.status == 3):
            update_status.append(img.url.urlhash)
            returls[img.url.urlhash] = img
        del goodurls[img.url.urlhash]
    del existing_urls_list
    Urls.objects.filter(
        urlhash__in=update_status
    ).update(
        urlhash=0
    )
    del update_status
    #insert new items to db
    for imghash, img in goodurls.iteritems():
        if not returls[imghash]:
            tmp_img_url = Urls()
            tmp_img_url.urlhash = hash
            tmp_img_url.url = img
            tmp_img_url.status = 0
            tmp_img_url.save()
            tmp_img = Images()
            tmp_img.ext = splitext(img)[1]
            tmp_img.page = page
            tmp_img.url = tmp_img_url
            tmp_img.save()
            returls[imghash] = tmp_img
            del goodurls[imghash]
    del goodurls
    return returls


def getPages():
    return list(
        Pages.objects.filter(
            Q(page__url__status=0) | Q(page__url__status=3)
        )
    )


def MainLoop():
    while True:
        sleep(0.1)
        try:
            pages = getPages()
            if not pages:
                continue
            #images to download
            images_hashes = {}
            for page in pages:
                tmp_img_hsh = addImagesFromPage(page)
                for hash in tmp_img_hsh.keys():
                    images_hashes[hash] = tmp_img_hsh[hash]
                tmp_img_hsh = None
            if not images_hashes:
                continue
            #it's not a bug but feature
            for hash in sorted(
				images_hashes.keys(),
				key=lambda x: random.random()
			):
                img = images_hashes[hash]
                fetchImg(img, savedir, maxsize)
                del img
                del images_hashes[hash]
        except:
            #TODO:add logging here
            pass

if __name__ == "__main__":
    MainLoop()



















