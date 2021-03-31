# Generated by Django 2.2.19 on 2021-03-31 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200825_0653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Pigskin User Profile'},
        ),
        migrations.AddField(
            model_name='user',
            name='PickConfirmation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='Reminder48',
            field=models.BooleanField(default=True),
        ),
    ]
