# Generated by Django 3.1.6 on 2021-08-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.FileField(upload_to='streaming/'),
        ),
    ]
