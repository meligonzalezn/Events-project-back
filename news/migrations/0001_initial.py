# Generated by Django 4.0.5 on 2022-07-16 22:52

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Summary', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=20)),
                ('Media_file', cloudinary.models.CloudinaryField(max_length=255)),
                ('Edition_date', models.DateField()),
                ('Finish_date', models.DateField()),
                ('ID_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('ID_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
