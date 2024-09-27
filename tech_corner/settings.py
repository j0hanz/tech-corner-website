"""Django settings for tech_corner project."""

import os
from datetime import timedelta
from pathlib import Path

import dj_database_url
from django.contrib.messages import constants as messages
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the secret key from environment variables
SECRET_KEY = os.getenv('SECRET_KEY')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Other settings...
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    '.gitpod.io',
    '127.0.0.1',
    'localhost',
    '.herokuapp.com',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'django.contrib.sites',
    'cloudinary',
    'axes',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_summernote',
    'website',
    'userprofile',
]

SITE_ID = 1

# Redirects after login/logout to the homepage "/"
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Django Crispy Forms settings
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'tech_corner.urls'

# Templates settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

# Maps alert message to Bootstrap CSS classes.
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# WSGI application
WSGI_APPLICATION = 'tech_corner.wsgi.application'

# Database
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        },
    }
    print('SQLite database')
else:
    DATABASES = {
        'default': dj_database_url.config(default=os.getenv('DATABASE_URL')),
    }
    print('Production database')

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    'https://*.codeinstitute-ide.net',
    'https://*.herokuapp.com',
]

# Password validation
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

# Authentication settings
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Django Axes configurations
# Secures login attempts by limiting failures and locking out users.
AXES_FAILURE_LIMIT = 5
AXES_LOCK_OUT_AT_FAILURE = True
AXES_COOLOFF_TIME = timedelta(minutes=30)
AXES_LOCKOUT_URL = '/lockout/'
AXES_RESET_ON_SUCCESS = True
AXES_LOCKOUT_PARAMETERS = ['username']

# Account settings
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Stockholm'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Cloudinary settings
CLOUDINARY_STORAGE = {'CLOUDINARY_URL': os.getenv('CLOUDINARY_URL')}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
