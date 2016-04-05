import os

from .application import PROJECT_ROOT_DIR


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'media')
