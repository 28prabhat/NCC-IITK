from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(StudentDetail)
admin.site.register(CampDetail)

@admin.register(Certificate)
class certificateadmin(admin.ModelAdmin):
    list_display=["DOB"]

