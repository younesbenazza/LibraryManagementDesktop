from pathlib import Path
import os
import sys
import shutil

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Detect if the app is running as a bundled executable (PyInstaller)
if getattr(sys, 'frozen', False):
    # Path to the folder where the PyInstaller bundle is extracted
    BASE_DIR = Path(sys._MEIPASS)
else:
    # For normal running, use the original BASE_DIR
    BASE_DIR = Path(__file__).resolve().parent.parent

# Set a writable directory for the database when the app is bundled (e.g., AppData on Windows)
DB_DIR = Path(os.getenv('APPDATA', BASE_DIR)) / 'MyApp'
DB_DIR.mkdir(parents=True, exist_ok=True)

# Path to the database in the writable directory
DB_PATH = DB_DIR / 'db.sqlite3'

# If the database doesn't exist in the writable directory, copy it from the bundled files
if not DB_PATH.exists():
    shutil.copyfile(BASE_DIR / 'db.sqlite3', DB_PATH)

# Quick-start development settings - unsuitable for production
SECRET_KEY = "django-insecure-99tx@n_im9*sfd1)s_r!tdg46p!xw)4h#*&7$gbo*5a)6a4_9m"

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Includes 'static/build/'
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For collectstatic command

# Application definition
INSTALLED_APPS = [
    "corsheaders",
    "rest_framework",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp",
    "rest_framework_simplejwt",
    "account",
    "libr",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5137",  # React dev server
    "http://127.0.0.1:8000",  # Django server
]

ROOT_URLCONF = "libr.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'libr', 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "libr.wsgi.application"

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DB_PATH,  # Use the copied or existing database path
    }
}

# Configuration of project
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
