# Django settings for saxs_deployment_apache project.
import  ConfigParser
from django.core.exceptions import ImproperlyConfigured
import os

# Set Global Defaults
PROJECT_NAME = 'saxs_deployment_apache'
THIS_FILE_PATH = os.path.abspath(os.path.split(__file__)[0])
PROJECT_PATH = THIS_FILE_PATH
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Some standard Django settings.
TIME_ZONE = 'UTC'  # Django uses the system timezone.
LANGUAGE_CODE = 'en-us' # Language code for this installation.
USE_I18N = True # Enable Django's internationalization system.

# Obatin the configuration from a file or set defaults
file_name = 'saxs-deployment-apache.ini'
config_path = '/etc/saxs/'
config_file = os.path.join(config_path, file_name)
config = ConfigParser.RawConfigParser()
config.read(config_file)

# matplotlib module configuration                               
MATPLOTLIB_HOME = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')


try:
    
    # Data path
    PROFILE_HOME = config.get('data','PROFILE_HOME')

    DEBUG = config.getboolean('debug','DEBUG')
    
    DATABASES = {
        'default': {
            # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'ENGINE': config.get('database', 'DATABASE_ENGINE'),
            # Name of the database to use. For SQLite, it's the full path.
            'NAME': config.get('database', 'DATABASE_NAME'),
            'USER': config.get('database', 'DATABASE_USER'),
            'PASSWORD': config.get('database', 'DATABASE_PASSWORD'),
            'HOST': config.get('database', 'DATABASE_HOST'),
            'PORT': config.get('database', 'DATABASE_PORT'),
        }
    }
except ConfigParser.NoSectionError, e:
    raise ImproperlyConfigured(e)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    )

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'saxs_style_glareindark',
    'saxs_library_js',
    'saxs_model_analysis',
    'saxs_app_analysis',
    )

# Configuration for the apps
ROOT_URLCONF = 'saxs_deployment_apache.urls'


