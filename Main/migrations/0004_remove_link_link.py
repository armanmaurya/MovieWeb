# Generated by Django 4.1.2 on 2022-11-09 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_link_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='link',
        ),
    ]