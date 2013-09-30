# coding=utf-8
from random import random, shuffle
from bs4 import BeautifulSoup
from django.db.models import Q
from ifwm.home.helpClasses import getTime, getMD5Str, dbgOut
from ifwm.home.models import Pages, Urls, Images
from time import sleep
from ifwm import settings
import os.path
import re
import traceback
import urllib2
import urlparse

#works
def StartCrawler():
    dbgOut('CrawlerRequested', 0)
    glb = globals()
    if not ('CrawlerStarted' in vars() or 'CrawlerStarted' in glb):
        glb['CrawlerStarted'] = True
        dbgOut('Crawler started', 3)
        from threading import Thread

        glb['thread'] = Thread(target=_MainLoop)
        glb['thread'].start()


#works
def urlopenUA(url):
    request = urllib2.Request(url=url, headers={'User-Agent': "Magic Browser"})
    return urllib2.urlopen(request, timeout=3000)


#works
def _parseIntOrZero(string):
    try:
        return int(string)
    except:
        return 0


#works
def _getPages():
    return list(
        Pages.objects.filter(
            Q(url__status=0) | Q(url__status=3)
        )
    )


#works
def _copyStream(read_stream, write_stream, count):
    downloaded = 0
    buffersize = 16384
    try:
        while downloaded < count:
            writebuf = read_stream.read(buffersize)
            if not writebuf:
                break
            downloaded += len(writebuf)
            write_stream.write(writebuf)
    finally:
        read_stream.close()
        write_stream.close()


#works
def _findImageUrlsOnPage(page_str):
    parser = BeautifulSoup(page_str)
    imgurls = []
    for img in parser.find_all('img'):
        imgurls.append(
            img.get('src')
        )
    del parser
    return imgurls


#works
def _filterDomainImages(imgurls, pageurl):
    finurls = {}
    pagehost = '.'.join(
        urlparse.urlparse(pageurl).netloc.split('.')[-2:]
    )
    for img in imgurls:
        try:
            o = urlparse.urlparse(img)
        except:
            o = ''
        nl = o.netloc
        if nl == '':
            curl = urlparse.urljoin(pageurl, o.path)
        elif nl == pagehost or nl.endswith('.' + pagehost):
            curl = img
        else:
            curl = None
        del o
        if not curl:
            continue
        curl = curl.replace('\\', '/') # urllib2 workaround
        imghash = getMD5Str(curl)
        #distinct
        if imghash in finurls:
            continue
        finurls[imghash] = curl
        del curl
    del imgurls
    return finurls


def _fetchImg(img, save_dir):
    try:
        dbgOut(
            'Downloading image "%s"  to %d' % (img.url.url, img.url.id),
            0
        )
        url = img.url
        url.status = 1
        url.save()
        image_response = urlopenUA(url.url)
        #region check size
        try:
            size_str = image_response.headers['content-length']
        except KeyError:
            size_str = '0'
        size = _parseIntOrZero(size_str)
        url.date = getTime()
        content_type = image_response.headers['content-type']
        if (
                (size > settings.MAX_FETCH_IMAGE_SIZE) or (
                    not content_type
                ) or (
                    not content_type.startswith('image/')
                )
        ):
            dbgOut('Banned image "%s"' % img.url.url, 1)
            url.status = 4
            return
            #extension
        if img.ext:
            ext = img.ext
        else:
            ext = '.' + re.search(
                'image/(\w+)',
                content_type
            ).group(0)
        save_filename = os.path.join(save_dir, str(url.id) + ext)
        write_stream = open(save_filename, 'wb')
        if size == 0:
            max_dwnld = settings.MAX_FETCH_IMAGE_SIZE
        else:
            max_dwnld = size
        try:
            _copyStream(image_response, write_stream, max_dwnld)
            dbgOut('Successfully downloaded image %s' % img.url.url, 0)
        except Exception, e:
            os.remove(save_filename)
            raise e
        url.status = 2
    except:
        traceback.print_exc()
        dbgOut(
            'Error occurred while downloading %s' % img.url.url,
            1
        )
        url.status = 3
    finally:
        url.save()

#find queued images and add to DB
#return their urls

#works
def _addImagesFromPage(page):
    try:
        page.url.status = 1
        page.url.save()
        pageurl = page.url.url
        dbgOut('Downloading page "%s"' % pageurl, 1)
        result = urlopenUA(pageurl)
        returls = {}
        #check size
        #ban big pages and not web pages
        if 'content-length' in result.headers:
            str_size = result.headers['content-length']
            size = _parseIntOrZero(str_size)
        else:
            size = 0
        page.url.date = getTime()
        if size > settings.MAX_FETCH_PAGE_SIZE or (
            not result.headers['content-type'].startswith('text/')
        ):
            dbgOut('Banned page "%s"' % page.url.url, 2)
            page.url.status = 4
            page.url.save()
            return returls
            #get urls
        parsetext = result.read()
        imgurls = _findImageUrlsOnPage(parsetext)
        del result
        if not imgurls:
            return returls
            #find urls to this domain + subdomains
        goodurls = _filterDomainImages(
            imgurls,
            pageurl
        )
        del imgurls
        if not goodurls:
            return returls
        dbgOut('Got %d images from page "%s"' % (len(goodurls), page.url.url), 0)
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
            if img.url.status == 3 or img.url.status == 0:
                dbgOut(
                    'Url with hash %s added to update list' % img.url.url, 0
                )
                update_status.append(img.url.urlhash)
                returls[img.url.urlhash] = img
            del goodurls[img.url.urlhash]
        del existing_urls_list
        if update_status:
            Urls.objects.filter(
                urlhash__in=update_status
            ).update(
                status=0
            )
        del update_status
        #insert new items to db
        #TODO: move all to one transaction
        #rolled back
        for imghash, img in goodurls.iteritems():
            if not imghash in returls:
                dbgOut(
                    'Url with hash %s added to download list' % imghash,
                    0
                )
                tmp_img_url = Urls()
                tmp_img_url.urlhash = imghash
                tmp_img_url.url = img
                tmp_img_url.status = 0
                tmp_img_url.save()
                tmp_img = Images()
                tmp_img.ext = os.path.splitext(tmp_img_url.url)[1]
                tmp_img.url = tmp_img_url
                tmp_img.save()  # many-to-many workaround
                tmp_img.page.add(page)
                tmp_img.save()
                returls[imghash] = tmp_img
        del goodurls
        dbgOut(
            'Parsing %s complete' % page.url.url,
            0
        )
        return returls
    except urllib2.URLError, e:
        if not hasattr(e, "code"):
            raise
        if e.code == 404:
            page.url.status = 4
            page.url.save()
            page.save()
    except:
        traceback.print_exc()
        page.url.status = 3
        page.url.save()
        page.save()

#works
def _MainLoop():
    dbgOut('Crawler works', 3)
    while True:
        sleep(5)
        Pages.objects.update()
        Urls.objects.update()
        Images.objects.update()
        try:
            dbgOut('Fetching pages from DB', 1)
            pages = _getPages()
            dbgOut('Got %d pages from DB' % len(pages), 0)
            if not pages:
                continue
                #images to download
            images_hashes = {}
            for page in pages:
                tmp_img_hsh = _addImagesFromPage(page)
                if not tmp_img_hsh:
                    continue
                for imghash in tmp_img_hsh.keys():
                    images_hashes[imghash] = tmp_img_hsh[imghash]
                del tmp_img_hsh
                dbgOut('Got %d images' % len(images_hashes), 0)
                if not images_hashes:
                    continue
                keys = images_hashes.keys()
                shuffle(keys)
                for imghash in keys:
                    img = images_hashes[imghash]
                    _fetchImg(img, settings.MEDIA_ROOT)
                    del img
                    del images_hashes[imghash]
                page.url.status = 2
                page.url.save()
        except:
            traceback.print_exc()
            continue
