# Generated by Django 3.1.3 on 2021-08-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automated_main', '0017_uitestresult_ui_test_script'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uitestresult',
            name='ui_test_script',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='UI测试脚本'),
        ),
    ]
