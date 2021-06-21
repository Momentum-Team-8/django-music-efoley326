# Generated by Django 3.2.4 on 2021-06-21 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mainForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=255)),
                ('artist_name', models.CharField(blank=True, max_length=300, null=True)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
