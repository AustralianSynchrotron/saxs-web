# Django settings for saxs_model_analysis project.
import os

# Set Global Defaults
PROJECT_NAME = 'saxs_model_analysis'
THIS_FILE_PATH = os.path.abspath(os.path.split(__file__)[0])
PROJECT_PATH = THIS_FILE_PATH

# Some standard Django settings.
TIME_ZONE = 'UTC'  # Django uses the system timezone.
LANGUAGE_CODE = 'en-us' # Language code for this installation.
USE_I18N = True # Enable Django's internationalization system.

DATABASES = {
    'default': {
        # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Name of the database to use. For SQLite, it's the full path.
        'NAME': '/tmp/saxs.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

INSTALLED_APPS = (
    'saxs_model_analysis',
)
