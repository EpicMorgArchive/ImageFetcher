#! /usr/bin/env python2.7



def get_debug():
    debug = True
    return debug


def getTEMPLATE_DEBUG():
    return get_debug()


def get_databases():
    databases = {
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
    return databases