# Generated by Django 2.1.7 on 2019-06-10 20:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('predictor', '0017_auto_20190610_2012'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='prediction',
            unique_together={('User', 'Game')},
        ),
    ]
