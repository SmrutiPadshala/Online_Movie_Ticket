from django.contrib import admin

# Register your models here.
from .models import UserBook,BookedSeatsModel

admin.site.register(UserBook)
admin.site.register(BookedSeatsModel)
