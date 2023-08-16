import os
MYSQL_AZURE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DBNAME'),
        'HOST': os.environ.get('DBHOST'),
        'USER': os.environ.get('DBUSER'),
        'PASSWORD': os.environ.get('DBPASS'),
    }
}

MYSQL_LOCAL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "django_chat",
        'HOST': "127.0.0.1",
        'USER': "root",
        'PASSWORD': "root",
    }

}