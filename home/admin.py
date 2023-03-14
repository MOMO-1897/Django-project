from django.contrib import admin

# Register your models
from .models import  *
admin.site.register(feedback)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Information)
