# Generated by Django 4.0.4 on 2022-06-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_activity_event_payment_news_event_payments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Media_file',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
