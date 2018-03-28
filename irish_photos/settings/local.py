from .base import *

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SYSTEM_EMAIL = 'development@retrocomputer.com'