import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'supersecretkey'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

BOM_CONFIG = {
    # docs: https://api.mouser.com/api/docs/ui/index
    'mouser_api_key': '1d412cfb-ec4b-4655-906b-46dcaaf30e5e', # via https://www.mouser.com/MyMouser/MouserSearchApplication.aspx
}

# google GoogleOAuth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'google_oauth2_key'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'secret_google_key'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else :
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
