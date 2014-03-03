import os
import sys
sys.path.append('/opt/webapp/slaser')
os.environ['DJANGO_SETTINGS_MODULE'] = 'slaser.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
