# Generated by Django 4.2.5 on 2023-10-06 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_userprofileinfo_coin_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cointransaction',
            name='email',
        ),
    ]
