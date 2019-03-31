from django.contrib import admin
from .models import Company, Charge, Director

# Register your models here.
admin.site.register(Company)
admin.site.register(Director)
admin.site.register(Charge)
