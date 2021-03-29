"""
Django settings for SHIProj project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os #we will use this for media and static folder in the app
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates') #integrating template folder

# STATIC_DIR = os.path.join(BASE_DIR, 'static')#integrating static folder



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*svhxkru#4ck*jn$1*3rkxlm@f0b3qn!t)+^4epx+$oz#=%pad'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.searchhomesindia.com', '184.168.127.141'] #url of godaddy
# ALLOWED_HOSTS = ['.searchhomesindia.com', '143.110.250.221'] #url of digitalocean
# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'SHIApp',   #configuring our app name 
    'rest_framework',  # this is the rest framework we are using for Rest APi Services
 
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SHIProj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR], #giving the info of our template folder to the django.
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

WSGI_APPLICATION = 'SHIProj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#This is the database info where we are using the postgresql database it is being used in server so don't delete it.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'searchhomedb',  #database name
        'USER': 'master',  #username
        'PASSWORD': 'H@ome@5',  #password
        'HOST': 'localhost',  #hostname
        'PORT': '', #portname
    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'SHIdb',  #database name
#         'USER': 'postgres',  #username
#         'PASSWORD': 'postgresql',  #password
#         'HOST': 'localhost',  #hostname
#         'PORT': '', #portname
#     }
# }





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


# Internat
# ionalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


#This is used to access the css,jsvascript and static image files in the project.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

#This is used to access the image files from the project which has been uploaded by using the django admin panel.
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'
# STATICFILES_DIRS = [STATIC_DIR, ]


# GOOGLE_RECAPTCHA_SECRET_KEY = '6LfuBLIUAAAAACBB_qClgqkR3RVjTmvWusQ8yNpJ'


