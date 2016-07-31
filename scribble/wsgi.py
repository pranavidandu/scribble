import os
import sys

# assuming your django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/pranavidandu/scribble/scribble'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'wildblogger.settings'

## Uncomment the lines below depending on your Django version
###### then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
