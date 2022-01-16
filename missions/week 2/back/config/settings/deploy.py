from .base import *

SECRET_KEY = 'django-insecure-yba6n*3l^350kxcj_gw@fnmew0#ea3z$omo373%2)@)i2+0dx!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mutbly_db',
        'USER': 'root',
        'PASSWORD': 'rootpass',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
