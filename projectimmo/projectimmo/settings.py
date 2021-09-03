"""
Django settings for projectimmo project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a_rl=nhjb+2-vc#k(e75lxtg@m0__r$s4^hokm7uwsw9i-c^1+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
#    'accounts',
#    'Mydiary',
    'django_filters',
    'address',
    'django_drf_filepond',
    'places',
    'account',
    'widget_tweaks',
    "verify_email",
    'datapackage',
    'multiselectfield',
    'stripe',
    'streaming_app',
    'mathfilters',
    'sslserver',
    'ffmpeg',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
GOOGLE_API_KEY = 'AIzaSyD1lHVWM1UP-2-F2RPwgBCcRKjYjXAqm5A'
PLACES_MAPS_API_KEY='AIzaSyD1lHVWM1UP-2-F2RPwgBCcRKjYjXAqm5A'
PLACES_MAP_WIDGET_HEIGHT=480
PLACES_MAP_OPTIONS='{"center": { "lat": 38.971584, "lng": -95.235072 }, "zoom": 10}'
PLACES_MARKER_OPTIONS='{"draggable": true}'
DJANGO_DRF_FILEPOND_FILE_STORE_PATH = os.path.join(BASE_DIR, 'static/documents')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'hamza.aboudou@gmail.com'
EMAIL_HOST_PASSWORD = 'Hahajonathanurbanginmydaughter47789!$?   '
CLIENT_AUTH_ID = '589f0450-92fa-467a-8215-608f808bb114'
CLIENT_SECRET_KEY = 'c44217a9-247a-4ca3-9611-81d6e208a03b'
STRIPE_SECRET_KEY = 'sk_test_51IvMHVEdIN3Y8UWsFM2nj0EiMamYqblY8bTlUDJ5xufHplnMXPUj2FAqJGaRqwYFpjdkHG06BnbnlRiN5yWpygGF00NhBQ1Zjx'
STRIPE_PUBLIC_KEY = 'pk_test_51IvMHVEdIN3Y8UWsWDpM9Ts0d8Q2JkN5Qynoqr5EwWWccryIbDAfDAe7l8m4IZr2CggENbYg9e1s5ypq2n4b3zWu004VTPrL85'
STRIPE_WEBHOOK_SECRET = 'whsec_LKxhJye0Zoi3UHzQkZijQGH5Oi4umopg'

DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projectimmo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_USER_MODEL = 'account.Account'

WSGI_APPLICATION = 'projectimmo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/images')

SECURE_SSL_REDIRECT = False