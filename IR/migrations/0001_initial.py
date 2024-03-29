# Generated by Django 4.1.3 on 2024-01-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('english', 'English'), ('arabic', 'العربيّة')], max_length=20)),
                ('retrieval_model', models.CharField(choices=[('boolean', 'Boolean Model'), ('extended_boolean', 'Extended Boolean Model'), ('vector', 'Vector Model')], max_length=20)),
                ('documents', models.JSONField()),
            ],
        ),
    ]
