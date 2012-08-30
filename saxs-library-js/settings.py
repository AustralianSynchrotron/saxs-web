# Django settings for saxs_library_js project.
import os

# Set Global Defaults
PROJECT_NAME = 'saxs_library_js'
THIS_FILE_PATH = os.path.abspath(os.path.split(__file__)[0])
PROJECT_PATH = THIS_FILE_PATH

# Some standard Django settings.
TIME_ZONE = 'UTC'  # Django uses the system timezone.
LANGUAGE_CODE = 'en-us' # Language code for this installation.
USE_I18N = True # Enable Django's internationalization system.

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
ADMIN_MEDIA_PREFIX = '/admin/media/' # Required as it defaults to /media
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Configuration for the apps
ROOT_URLCONF = 'urls'
INSTALLED_APPS = (
    'saxs_style_glareindark',
    'saxs_library_js',
)
