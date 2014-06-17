from django.contrib import admin
from core.models import Agency


class AgencyAdmin(admin.ModelAdmin):
  fields = ('full_name', 'short_name')

admin.site.register(Agency, AgencyAdmin)