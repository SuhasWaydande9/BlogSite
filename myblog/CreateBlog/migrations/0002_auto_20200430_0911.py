# Generated by Django 3.0.5 on 2020-04-30 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateBlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='categories',
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('comedy', 'comedy'), ('romantic', 'romantic'), ('mystery', 'mystery'), ('horror', 'horror'), ('mythology', 'mythology'), ('normal', 'normal')], default='normal', max_length=30),
        ),
    ]
