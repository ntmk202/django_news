from django.contrib import admin
from newsApp import models
from parler.admin import TranslatableAdmin
# Register your models here.

admin.site.register(models.Category, TranslatableAdmin)
admin.site.register(models.Post, TranslatableAdmin)
admin.site.register(models.Comment, TranslatableAdmin)
admin.site.register(models.Banner)
admin.site.register(models.Video, TranslatableAdmin)
admin.site.register(models.MediaPg, TranslatableAdmin)