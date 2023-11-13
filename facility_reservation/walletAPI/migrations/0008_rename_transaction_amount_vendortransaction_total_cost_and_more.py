# Generated by Django 4.2.5 on 2023-11-08 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walletAPI', '0007_alter_vendortransaction_transaction_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendortransaction',
            old_name='transaction_amount',
            new_name='total_cost',
        ),
        migrations.RemoveField(
            model_name='vendortransaction',
            name='description',
        ),
        migrations.RemoveField(
            model_name='vendortransaction',
            name='transaction_date',
        ),
        migrations.RemoveField(
            model_name='vendortransaction',
            name='transaction_id',
        ),
        migrations.AddField(
            model_name='vendortransaction',
            name='BookDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='vendortransaction',
            name='computers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vendortransaction',
            name='endTime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='vendortransaction',
            name='purpose',
            field=models.CharField(default='Studying', max_length=50),
        ),
        migrations.AddField(
            model_name='vendortransaction',
            name='startTime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='vendortransaction',
            name='venueName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vendortransaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]