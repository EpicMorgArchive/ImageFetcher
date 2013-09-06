"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import time
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from ifwm.home.models import Pages, Images, Urls, Relations
from django.shortcuts import get_object_or_404
from django.core.validators import URLValidator

class SimpleTest(TestCase):
    def test_basic_addition(self):
		url = Urls()