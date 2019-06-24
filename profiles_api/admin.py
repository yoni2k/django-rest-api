from django.contrib import admin
from profiles_api import models

# Register our UserProfile with admin site and make it available through admin interface
admin.site.register(models.UserProfile)
