# Generated by Django 3.0.14 on 2022-04-05 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20220402_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='starting_bid',
            new_name='price',
        ),
    ]