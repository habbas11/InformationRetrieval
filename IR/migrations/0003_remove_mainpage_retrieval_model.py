# Generated by Django 4.1.3 on 2024-01-02 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IR', '0002_searchpagemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpage',
            name='retrieval_model',
        ),
    ]
