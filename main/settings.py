import os

if os.environ.get("DJANGO_ENV") == "PRODUCTION":
    from .prod_settings import *
else:
    from .dev_settings import *
