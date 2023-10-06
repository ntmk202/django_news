from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.
class Partner(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'),max_length=50)
    )
    logo = models.ImageField(upload_to="partners_logo")

class AboutContent(TranslatableModel):
    translations = TranslatedFields(
        content = RichTextField(_('content'))
    )

class Resource(TranslatableModel):
    translations = TranslatedFields(
        title = models.TextField(_('title'))
    )
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')

    def get_absolute_url(self):
        return self.file.url

    def __str__(self):
        return self.title 