import os

from .application import BASE_DIR


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'seongpil',
        'USER': 'seongpil',
    }
}
