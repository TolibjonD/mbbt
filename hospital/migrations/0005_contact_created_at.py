# Generated by Django 4.0 on 2023-05-11 03:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
