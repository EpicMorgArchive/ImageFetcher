#! /usr/bin/env python2.7

def getDEBUG():
	DEBUG = True
	return DEBUG
def getTEMPLATE_DEBUG():
 	return getDEBUG()

def getDATABASES():
	DATABASES = {
	    'default': {
	        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': 'ifwm',
	        # The rest is not used with sqlite3:
	        'USER': 'ifwm',
	        'PASSWORD': 'zYAweLfdwRYFTQQW',
	        'HOST': '192.168.1.1',
	        'PORT': '',
	    }
	}
	return DATABASES