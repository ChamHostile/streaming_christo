# Generated by Django 3.1.6 on 2021-08-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_app', '0003_auto_20210804_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='file_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
