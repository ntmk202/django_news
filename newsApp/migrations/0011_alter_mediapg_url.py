# Generated by Django 4.0.3 on 2023-11-09 06:18

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0010_alter_mediapg_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediapg',
            name='url',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Video url'),
        ),
    ]
