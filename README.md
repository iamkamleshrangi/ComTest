# ComTest

Reset Migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

Shell 
/manage.py shell
from django.contrib.auth.models import User
from roc.models improt Company
