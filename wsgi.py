"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

#application = get_wsgi_application()

from helloflask import app as application

if __name__=='__main__':
   from wsgiref.simple_server import make_server
   httpd=make_server('localhost',8051,application)
   httpd.handle_request()
