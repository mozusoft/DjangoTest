from django.contrib import admin
from students.models import *

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name','city','street','home']

admin.site.register(Student)
# admin.site.register(Region)
# admin.site.register(City)
admin.site.register(Place,PlaceAdmin)

