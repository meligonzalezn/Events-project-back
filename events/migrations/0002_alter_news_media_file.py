# Generated by Django 4.0.4 on 2022-06-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Media_file',
            field=models.FileField(upload_to='images_videos_news/'),
        ),
    ]
