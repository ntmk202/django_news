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