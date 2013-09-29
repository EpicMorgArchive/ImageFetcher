#! /usr/bin/env python2.7
import os
import sys
from mconf import *

#media_root relative part
IMAGE_SAVE_REAL_PATH = 'staticfiles/media/'
#media_url relative part to STATIC_URL
IMAGE_SAVE_WEB_PATH = 'media'
#max page size to parse
MAX_FETCH_PAGE_SIZE = 512*1024
#max image size to fetch
MAX_FETCH_IMAGE_SIZE = 4*1024*1024
#log level
DBG_OUT_LEVEL = 0

DEBUG = get_debug()
TEMPLATE_DEBUG = DEBUG
DATABASES = get_databases()
ALLOWED_HOSTS = [
    '*'  # debug
]
ABSOLUTE_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
ABSOLUTE_TEMPLATES_PATH = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'templates/'))

if not ABSOLUTE_PROJECT_ROOT in sys.path:
    sys.path.insert(0, ABSOLUTE_PROJECT_ROOT)
    
STATIC_ROOT = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'static/'))
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, IMAGE_SAVE_REAL_PATH))

# URL that handles the media, static, etc.
STATIC_URL = 'static/'
MEDIA_URL = STATIC_URL + IMAGE_SAVE_WEB_PATH

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(ABSOLUTE_PROJECT_ROOT, 'staticfiles/')),
)
ADMINS = (
    ('kasthack', 'kasthack@epicm.org'),
)
MANAGERS = ADMINS
#localization settings
TIME_ZONE = None
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
#installed app cofnig
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
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

