from django.contrib import admin
#from . import models
from .models import MovieMaster,AdminSide,SetMovie
# Register your models here.
admin.site.register(MovieMaster)
admin.site.register(AdminSide)
admin.site.register(SetMovie)