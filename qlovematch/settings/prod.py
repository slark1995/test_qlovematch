# flake8: noqa
import pymysql

pymysql.install_as_MySQLdb()

from .base import *  # noqa: F403

# from kombu import Exchange, Queue

DEBUG = False
IS_DEV = False
ALLOWED_HOSTS = ['*']

# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     }
# }
# END CACHE CONFIGURATION

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qlovematch',
        'USER': 'root',
        'PASSWORD': 'fenfen',
        'HOST': '139.224.212.27',
        'PORT': '3306',
        'OPTIONS': {
            # mysql < 5.7 [storage_engine], mysql >= 5.7 [default_storage_engine]
            'init_command': 'SET default_storage_engine=InnoDB',
            'sql_mode': 'STRICT_TRANS_TABLES',
            'charset': 'utf8mb4'
        }
    }
}
# END DATABASE CONFIGURATION

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# END EMAIL CONFIGURATION

# Determine which requests should render Django Debug Toolbar
INTERNAL_IPS = ('127.0.0.1',)

# SETTINGS FOR CELERY
BROKER_URL = ''
CELERY_RESULT_BACKEND = ''

# CACHE
try:
    CACHES['default']['LOCATION'] = ''
except Exception as e:
    pass

ENABLE_AUTO_AUTH = True

# Setting logging level
LOGGING['handlers']['default']['level'] = 'INFO'
LOGGING['handlers']['console']['level'] = 'DEBUG'

# settings for cronjobs
CRONTAB_DJANGO_SETTINGS_MODULE = 'qlovematch.settings.prod'

# Seperate Migrations
MIGRATION_MODULES = {app: '%s.prod_migrations' % app for app in MIGRATE_APPS}
