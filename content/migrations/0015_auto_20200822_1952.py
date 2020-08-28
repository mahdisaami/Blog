# Generated by Django 2.2 on 2020-08-22 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_auto_20200822_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='posts', to='content.Category', verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', through='content.PostTag', to='content.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='content.Post', verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_tag', to='content.Tag', verbose_name='tag'),
        ),
    ]
