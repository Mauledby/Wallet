# Generated by Django 4.2.5 on 2023-10-06 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_cointransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='coin_balance',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]