# Generated by Django 4.2.5 on 2023-10-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0010_adminpointaward'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='rfid_value',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
