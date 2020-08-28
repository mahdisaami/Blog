# Generated by Django 2.2 on 2020-08-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20200822_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='content.Category', verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', through='content.PostTag', to='content.Tag', verbose_name='tags'),
        ),
    ]
