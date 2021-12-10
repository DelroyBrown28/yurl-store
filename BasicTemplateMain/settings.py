from easy_thumbnails.conf import Settings as thumbnail_settings
import os
import dj_database_url
import environ
from pathlib import Path

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')


ALLOWED_HOSTS = ['nueui-basictemplate.herokuapp.com', 'localhost', '*']


INSTALLED_APPS = [
    # Jet Stuff
    'jet.dashboard',
    'jet',
    # Django Stuff
    'django.contrib.admin',
    'djrichtextfield',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'colorfield',
    'django_social_share',
    'phonenumber_field',
    'easy_thumbnails',
    'image_cropping',

    # Allauth Stuff
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Site Stuff
    'context_processors',
    'page_customisations',
    'home',
    'products',
    'bag',
    'checkout',
    'profiles',
    'about',
    'testimonials',
    # Other
    'crispy_forms',
    'storages',

]

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

SITE_ID = 1

JET_SIDE_MENU_COMPACT = True

X_FRAME_OPTIONS = 'SAMEORIGIN'

DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.tiny.cloud/1/ejfej7wzcg1hib8eew1onmh8d577qbpz8zcxwbb9ldzpk69m/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image textcolor',
        'toolbar': 'bold italic | link image | removeformat | forecolor backcolor',
        'width': 700
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'nueui-ecommerce-template'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static/'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media/'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'BasicTemplateMain.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap4'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'context_processors.context_processors.categories_processor',
                'context_processors.context_processors.add_testimonial_processor',
                'context_processors.context_processors.products_processor',
                'context_processors.context_processors.header_customisation_processor',
                'context_processors.context_processors.cta_processor',
                'context_processors.context_processors.product_banner_processor',
                'context_processors.context_processors.testimonials_customisation_processor',
                'context_processors.context_processors.testimonials_push',
                'context_processors.context_processors.footer_customisation_processor',
                'context_processors.context_processors.products_page_customisation_processor',
                'context_processors.context_processors.global_styles_processor',
                'bag.contexts.bag_contents',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

)

WSGI_APPLICATION = 'BasicTemplateMain.wsgi.application'


if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


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


LANGUAGE_CODE = 'en-us'

USE_TZ = True

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True


STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cache Control
AWS_S3_OBJECT_PARAMETERS = {
    # 'Expires': 'Thu, 31 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

# STRIPE STUFF
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10
STRIPE_CURRENCY = 'gbp'
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET')
STRIPE_ENDPOINT_SECRET = os.environ.get('STRIPE_ENDPOINT_SECRET')


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_POST = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FORM_EMAIL = os.environ.get('EMAIL_HOST_USER')


TINYMCE_JS_URL = 'https://cdn.tiny.cloud/1/ejfej7wzcg1hib8eew1onmh8d577qbpz8zcxwbb9ldzpk69m/tinymce/5/tinymce.min.js'
TINYMCE_COMPRESSOR = False
