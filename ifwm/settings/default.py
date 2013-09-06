#! /usr/bin/env python2.7
import os
import sys
from settings.mconf import *

DEBUG=getDEBUG()
TEMPLATE_DEBUG = DEBUG
DATABASES = getDATABASES()

ALLOWED_HOSTS = [
    '*' #debug
]

ABSOLUTE_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
ABSOLUTE_TEMPLATES_PATH = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'templates/'))

if not ABSOLUTE_PROJECT_ROOT in sys.path:
    sys.path.insert(0, ABSOLUTE_PROJECT_ROOT)

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'static/'))
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'staticfiles/media/'))

# URL that handles the media, static, etc.
STATIC_URL = '/static/'
MEDIA_URL = STATIC_URL + 'media/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'staticfiles/')),
)
ADMINS = (
    ('kasthack', 'kasthack@epicm.org'),
)
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = '(gs5&emc462$ai7$@@a1oxnt5_e0^qs=*cnrbxn&q#4zdu!(2h'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ifwm.urls'

WSGI_APPLICATION = 'wsgihandler.application'

TEMPLATE_DIRS = (
    ABSOLUTE_TEMPLATES_PATH,
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    # required by django-admin-tools
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

ADMIN_TOOL_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
)

CORE_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

EXTERNAL_APPS = (
    'south',
)

LOCAL_APPS = (
    'ifwm.home',
)

INSTALLED_APPS = ADMIN_TOOL_APPS + CORE_APPS + LOCAL_APPS + EXTERNAL_APPS

def _require_debug_false(request):
    from django.conf import settings
    return not settings.DEBUG
LOGGING = None
if DEBUG:
	LOGGING = {
	    'version': 1,
	    'disable_existing_loggers': False,
	    'filters': {
	        'require_debug_true': {
	           '()': 'django.utils.log.RequireDebugTrue',
	        },
	    },
	    'handlers': {
	        'console': {
	            'level': 'DEBUG',
	            'class': 'logging.StreamHandler',
	        },
	    },
	    'loggers': {
	        'django.request': {
	            'handlers': ['console'],
	            'level': 'ERROR',
	            'propagate': True,
	        },
	    }
	}
else:
	LOGGING = {
	    'version': 1,
	    'disable_existing_loggers': False,
	    'filters': {
	        'require_debug_false': {
	            '()': 'django.utils.log.CallbackFilter',
	            'callback': _require_debug_false
	        }
	    },
	    'handlers': {
	        'console': {
	            'level': 'DEBUG',
	            'class': 'logging.StreamHandler',
	        },
	    },
	    'loggers': {
	        'django.request': {
	            'handlers': ['console'],
	            'level': 'ERROR',
	            'propagate': True,
	        },
	    }
	}

