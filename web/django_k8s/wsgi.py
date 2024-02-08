"""
WSGI config for django_k8s project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import pathlib

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_k8s.settings")

application = get_wsgi_application()

application = WhiteNoise(application)
