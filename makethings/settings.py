import os
import os.path
from django.core.exceptions import ImproperlyConfigured

def get_env_var(name, **kwargs):
    try:
        return os.environ[name]
    except KeyError:
        if 'default' in kwargs:
            return kwargs['default']
        raise ImproperlyConfigured('Set the {} environment variable.'.format(name))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ola', 'ola@makerland.org'),
    ('Przemek', 'przemek@makerland.org')
)

MANAGERS = ADMINS

DATABASES = {}
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False
USE_L10N = True
USE_TZ = True


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = 'staticfiles/media'
MEDIA_URL = '/static/media/'

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-*k)im=cs%l6c*9x*$^xu-6xq7mso9w)d3ib7&amp;)@7wl(buxtsw'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)

ROOT_URLCONF = 'makethings.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'makethings.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, '../templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.i18n',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'suit',
    'django.contrib.admin',

    'south',

    'core',
    'event',
)

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Make Things',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True
}

try:
    from local_settings import *
except:
    pass

