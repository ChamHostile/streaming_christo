# Generated by Django 3.1.6 on 2021-08-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_account_photo_stream'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='packages_type',
            field=models.CharField(choices=[('BRON', 'Bronze'), ('SILV', 'Silver'), ('GOLD', 'Gold')], default='BRON', max_length=4, verbose_name='Package'),
        ),
    ]
