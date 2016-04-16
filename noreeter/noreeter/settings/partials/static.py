import os

from .application import PROJECT_ROOT_DIR


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'media')

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'style': {
            'source_filenames': (
                'sass/main.sass',
            ),
            'output_filename': 'css/main.css',
        },
        'vendor': {
            'source_filenames': (
                'css/vendor/bootstrap.css',
            ),
            'output_filename': 'css/vendor.css',
        },
    },
    'JAVASCRIPT': {
        'main': {
            'source_filenames': (
                'carousel.jquery.js',
                'js/main.js',
            ),
            'output_filename': 'js/noreeter.js',
        },
        'library': {
            'source_filenames': (
                'js/vendor/jquery-1.12.3.js',
            ),
            'output_filename': 'js/library.js',
        },
        'vendor': {
            'source_filenames': (
                'js/vendor/bootstrap.js',
            ),
            'output_filename': 'js/vendor.js',
        }
    },
    'COMPILERS': {
        'pipeline.compilers.sass.SASSCompiler',
    },
}

PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
