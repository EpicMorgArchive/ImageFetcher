#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url
from django.core import serializers
from django.core.validators import URLValidator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import simplejson
from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from ifwm.home.crawler import StartCrawler
from ifwm.home.helpClasses import *
from ifwm.home.models import Pages, Images, Urls
from django.core.context_processors import request

Validator = URLValidator()


def showErrorPage(request, errorname, errortext, status=200):
    errorpage = ErrorPageView()
    errorpage.request = request
    error = Error(errorname, errortext)
    return errorpage.showError(error, status)


def showImagesPage(request, url):
    ipage = ImagesPageView()
    ipage.request = request
    return ipage.showPage(url)


class ErrorPageView(TemplateView):
    template_name = 'error.html'

    def showError(self, error, status=200):
        StartCrawler()
        return render(
            self.request,
            self.template_name,
            {
                'error': error
            },
            status=status
        )


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        StartCrawler()
        return self.render_to_response({})


class AddUrlView(TemplateView):
    def _insertUrl(self, url, hasher):
        urlinfo = Urls()
        urlinfo.urlhash = hasher
        urlinfo.url = url
        urlinfo.save()
        page = Pages()
        page.url = urlinfo
        page.save()
        return urlinfo

    def post(self, request, *args, **kwargs):
        StartCrawler()
        url = request.POST.get('url', '')
        if not url:
            return showErrorPage(
                request,
                'Bad url',
                'Empty url',
                400
            )
        try:
            Validator(url)
        except:
            url = 'http://%s' % url
            try:
                Validator(url)
            except:
                return showErrorPage(
                    request,
                    'Bad url',
                    'Invalid url',
                    400
                )
        hasher = getMD5Str(url)
        dburls = Urls.objects.filter(urlhash=hasher)[:1]
        if dburls:
            urlinfo = dburls[0]
            #link to image
            if not Pages.objects.filter(url=urlinfo.id)[:1]:
                return showErrorPage(
                    request,
                    'Bad url',
                    'You are trying to add image',
                    400
                )
            if urlinfo.status == 4:
                return showErrorPage(
                    request,
                    'Bad url',
                    'This url was banned',
                    403
                )
            elif urlinfo.status == 2 | urlinfo.status == 3:
                urlinfo.status = 0
                urlinfo.save()
        else:
            try:
                urlinfo = self._insertUrl(url, hasher)
            except:
                return showErrorPage(
                    request,
                    'Bad url',
                    'Invalid url',
                    400
                )
        return redirect('/page%d' % urlinfo.id)


class ImagesPageView(TemplateView):
    template_name = 'image_list.html'

    def _showPage(self, url, page, *args, **kwargs):
        images = page.images_set.all().prefetch_related('url')
        imglist = list(images)
        context = {
            'page': page,
            'images': imglist,
            'url': url,
            'timestamp': getTime(),
            'args': args,
            'kwargs': kwargs
        }
        return self.render_to_response(context)

    def showPage(self, url):
        return self.showPageF(url, Pages.objects.get(pk=url.id))

    def showPageF(self, url, page):
        return self._showPage(url, page, None, None)

    def get(self, request, *args, **kwargs):
        StartCrawler()
        pageid = 0
        sid = kwargs.get('id')
        try:
            pageid = int(sid)
            page = Pages.objects.get(pk=pageid)
        except Exception, e:
            return showErrorPage(
                request,
                '404',
                'Nothing found',
                404
            )
        return self._showPage(
            page.url,
            page,
            args,
            kwargs
        )


class PageProgress(View):
    def _badReq(self):
        return HttpResponse(
            '{"result": "error" } ',
            mimetype='application/json',
            status=400
        )

    def resp(self, params):
        try:
            #parse
            sctimestamp = params.get('timestamp')
            spageid = params.get('pageid')
            ctimestamp = int(sctimestamp)
            pageid = int(spageid)
            sctimestamp = None
            spageid = None
            #date check
            timestamp = getTime()
            if ctimestamp > timestamp:
                return self._badReq()
            #db fetch
            page = Pages.objects.get(pk=pageid)
            images = page.images_set.exclude(
                url__status__lt=2
            ).filter(
                url__date__gte=ctimestamp
            ).prefetch_related('url')
            #jsonize
            pi = ProgressInfo(
                page,
                timestamp,
                images
            )
            return HttpResponse(
                pi.getJson(),
                mimetype='application/json'
            )
        except:
            return self._badReq()

    def post(self, request, *args, **kwargs):
        StartCrawler()
        return self.resp(request.POST)

    def get(self, request, *args, **kwargs):
        StartCrawler()
        return self.resp(request.GET)
