# Generated by Django 3.1.3 on 2021-06-23 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automated_main', '0009_auto_20210623_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uitestresult',
            name='result',
        ),
    ]
