# Generated by Django 3.1.6 on 2021-08-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_app', '0002_auto_20210804_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.FileField(blank=True, upload_to='streaming/'),
        ),
    ]
