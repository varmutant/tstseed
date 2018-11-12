from django.contrib import admin

from .models import MyEncrypt
from .models import MyDetail

admin.site.register(MyEncrypt)
admin.site.register(MyDetail)
