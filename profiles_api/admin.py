from django.contrib import admin
from profiles_api import models

# Register our UserProfile with admin site and make it available through admin interface
admin.site.register(models.UserProfile)

# to be able to administer Profile Feed Items in the Admin site
admin.site.register(models.ProfileFeedItem)
