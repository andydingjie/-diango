# Generated by Django 3.1.3 on 2021-06-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automated_main', '0006_performancescript_performance_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancescript',
            name='performance_script',
            field=models.CharField(max_length=5000, verbose_name='性能测试脚本'),
        ),
    ]