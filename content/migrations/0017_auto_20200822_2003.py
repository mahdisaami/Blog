# Generated by Django 2.2 on 2020-08-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_auto_20200822_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True, verbose_name='body'),
        ),
    ]
