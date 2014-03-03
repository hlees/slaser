"""
WSGI config for slaser project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
sys.path.append('/opt/webapp/slaser/slaser')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "slaser.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
