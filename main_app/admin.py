from django.contrib import admin
from .models import Character, Title, Medium 

# Register your models here.
admin.site.register(Character)
admin.site.register(Title)
admin.site.register(Medium)