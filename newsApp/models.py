from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


# Create your models here.
class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'),max_length=250),
    )
    status = models.CharField(_('status'),max_length=2, choices=(("1",_('Active')), ("2",_('Inactive'))), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Post(TranslatableModel):
    translations = TranslatedFields(
        title = models.TextField(_('title')),
        Description = models.TextField(_('short_description')),
        content = models.TextField(_('content')),
    )
    status = models.CharField(_('status'),max_length=2, choices=(("1",_('Published')), ("2",_('Unpublished'))), default=2)
    category = models.ForeignKey(Category, related_name=_('category'), on_delete=models.CASCADE,default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    banner_path = models.ImageField(_('banner_path'),upload_to='news_bannner')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

class Banner(models.Model):
    banner = models.ImageField(upload_to="banner_home")

class Comment(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'),max_length=250),
        subject = models.CharField(_('subject'),max_length=250),
        message = models.TextField(_('message'))
    )
    post = models.ForeignKey(Post, related_name=_('comment'), on_delete=models.CASCADE,default="")
    email = models.CharField(max_length=250)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.name} - {self.post.title}"
    
class Video(TranslatableModel):
    translations = TranslatedFields(
        title = models.TextField(_('title'))
    )
    url = EmbedVideoField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)

    def __st__(self):
        return str(self.title)

class MediaPg(TranslatableModel):
    translations = TranslatedFields(
        title = models.TextField(_('title'))
    )
    url = EmbedVideoField()
    postUrl = models.URLField(_('postUrl'))
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)

    def __st__(self):
        return str(self.title)