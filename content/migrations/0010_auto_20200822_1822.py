# Generated by Django 2.2 on 2020-08-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20200817_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(null=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='content.Category', verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', through='content.PostTag', to='content.Tag', verbose_name='tags'),
        ),
    ]
