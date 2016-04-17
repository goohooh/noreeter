import os

import dj_database_url

from .application import BASE_DIR


DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}
