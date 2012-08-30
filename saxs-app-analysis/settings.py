# Django settings for saxs_app_analysis project.
import os

# Set Global Defaults
PROJECT_NAME = 'saxs_app_analysis'
THIS_FILE_PATH = os.path.abspath(os.path.split(__file__)[0])
PROJECT_PATH = THIS_FILE_PATH

# Some standard Django settings.
TIME_ZONE = 'UTC'  # Django uses the system timezone.
LANGUAGE_CODE = 'en-us' # Language code for this installation.
USE_I18N = True # Enable Django's internationalization system.

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
ADMIN_MEDIA_PREFIX = '/admin/media/' # Required as it defaults to /media
STATIC_URL = '/static/'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
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

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

# matplotlib module configuration                               
MATPLOTLIB_HOME = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/') 

# Data path
PROFILE_HOME = '/tmp/'

# Configuration for the apps
ROOT_URLCONF = 'urls'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.messages',
    'saxs_style_glareindark',
    'saxs_library_js',
    'saxs_model_analysis',
    'saxs_app_analysis',
)
