# Generated by Django 5.1.6 on 2025-02-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.TextField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('weather_details', models.JSONField()),
            ],
        ),
    ]
