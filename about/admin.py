from django.contrib import admin

# Register your models here.
from about import models
from parler.admin import TranslatableAdmin
# Register your models here.

admin.site.register(models.Partner, TranslatableAdmin)
admin.site.register(models.AboutContent, TranslatableAdmin)
admin.site.register(models.Resource, TranslatableAdmin)