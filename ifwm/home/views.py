#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import time
from django.conf import settings
from django.core.validators import URLValidator
from django.http import HttpResponse
from django.views.generic import TemplateView
from ifwm.home.helpClasses import Error, ProgressInfo
from ifwm.home.models import Pages, Images, Urls
import django.utils.simplejson

Validator = URLValidator()

#enum Status
	#0	queued							:default
	#1	running							:downloading
	#2	complete						:complete
	#3	error							:error
	#4	banned							:denied
	#5	converting
def getTime():
	return int(time.time())
def showErrorPage(request, errorname, errortext):
	errorpage = ErrorPageView()
	errorpage.request=request
	error = Error(errorname, errortext)
	return errorpage.showError(error)
def showImagesPage(request, url):
	ipage = ImagesPageView()
	ipage.request=request
	return ipage.showPage(url)
def getMD5Str(inputStr):
	from hashlib import md5
	hasher = md5()
	hasher.update(inputStr)
	return hasher.hexdigest()

class ErrorPageView(TemplateView):
	template_name = 'error.html'
	def showError(self, error):
		context = {
			'error':error
		}
		return self.render_to_response(context)

class HomeView(TemplateView):
	template_name = 'home.html'

	def get(self, request, *args, **kwargs):
		context = {
			#'some_dynamic_value': 'This text comes from django view!',
		}
		return self.render_to_response(context)

class AddUrlView(TemplateView):
	
	def _insertUrl(self, url, hasher):
		urlinfo = Urls()
		urlinfo.urlhash=hasher
		urlinfo.url=url
		urlinfo.save()
		page = Pages()
		page.url = urlinfo
		page.save()
		return urlinfo
		
	def post(self, request, *args, **kwargs):
		url = request.POST.get('url','')
		if not url:
			return showErrorPage(request,"Bad url", "Empty url")
		try:
			Validator(url)
		except:
			url="http://%s" % url
		try:
			Validator(url)
		except:
			return showErrorPage(request,"Bad url", "Invalid url")
		hasher = getMD5Str(url)
		dburls = Urls.objects.filter(urlhash=hasher)[:1]
		if dburls:
			urlinfo = dburls[0]
			#link to image
			if not Pages.objects.filter(url=urlinfo.id)[:1]:
				return showErrorPage(request,"Bad url", "You are trying to add image")
			if urlinfo.status==4:
				return showErrorPage(request,"Bad url", "This url was banned")
			if urlinfo.status==2 | urlinfo.status==3:
				urlinfo.status = 0
				urlinfo.save()
		else:
			try:
				urlinfo = self._insertUrl(url, hasher)
			except:
				return showErrorPage(request,"Bad url", "Invalid url")
		return  showImagesPage(request, urlinfo)

class ImagesPageView(TemplateView):
	template_name = 'image_list.html'
	
	def _showPage(self, url, page, *args, **kwargs):
		images = page.images_set.all()
		images.prefetch_related('url')
		context = {
			'args': args,
			'kwargs' : kwargs,
			'page' : page,
			'images' : images,
			'url' : url,
			'timestamp' : getTime(),
		}
		return self.render_to_response(context)
	
	def showPage(self, url):
		return self.showPageF(url, Pages.objects.get(pk=url.id))
	
	def showPageF(self, url, page):
		return self._showPage(url, page, None, None)
	
	def get(self, request, *args, **kwargs):
		pageid = 0
		sid = kwargs.get('id')
		try:
			pageid = int(sid)
			page = Pages.objects.get(pk=pageid)
		except:
			return showErrorPage(request, "404", "Nothing found")
		return self._showPage(page.url, page, args, kwargs)
class PageProgress(TemplateView):
	
	def post(self, request, *args, **kwargs):
		try:
			ctimestamp = int(request.POST.get('timestamp',''))
			pageid = int(request.POST.get('page',''))
			page = Pages.objects.get(pk=pageid)
			images = page.images_set.filter(url.timestamp>=ctimestamp).all()
			images.prefetch_related('url')
			progress = ProgressInfo(page, getTime(), page.status, images)
			jsondata = simplejson.dumps(progress)
			return HttpReponse(jsondata,mimetype='application/json')
		except:
			return showErrorPage(request, "Bad request", "")
