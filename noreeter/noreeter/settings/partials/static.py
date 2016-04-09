import os

from .application import PROJECT_ROOT_DIR


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'media')

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'main': {
            'source_filenames': (
                'css/*.css',
            ),
            'Output_filename': 'css/noreeter.css',
        },
        'vendor': {
            'source_filenames': (
                'css/vendor/bootstrap.min.css',
            ),
            'Output_filename': 'css/vendor.css',
        },
    },
    'JAVASCRIPT': {
        'main': {
            'source_filenames': (
                'js/*.js',
            ),
            'output_filename': 'js/noreeter.js',
        },
        'vendor': {
            'source_filenames': (
                'js/vendor/bootstrap.min.js',
            ),
            'Output_filename': 'js/vendor.js',
        },
    },
}
