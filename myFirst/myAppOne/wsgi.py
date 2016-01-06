
import os
import sys
sys.path.append('/home/rahul/rahul/Django-Practise/myFirst')
sys.path.append('/home/rahul/rahul/Django-Practise/myFirst/myAppOne')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myAppOne.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
