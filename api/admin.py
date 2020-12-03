from django.contrib import admin
from .models import Shortener

class OrganizerAdmin(admin.ModelAdmin):
   
    fields = ('original_link',)


admin.site.register(Shortener,OrganizerAdmin)