from .base import *

DEBUG = False
ALLOWED_HOSTS = ['mipagina.com', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
os.environ['DJANGO_PORT']= '8080'