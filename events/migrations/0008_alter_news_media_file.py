# Generated by Django 4.0.4 on 2022-06-11 22:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_rename_id_event_news_id_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Media_file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images_videos_news/'),
        ),
    ]