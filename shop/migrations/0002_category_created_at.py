# Generated by Django 2.1.5 on 2019-01-29 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
