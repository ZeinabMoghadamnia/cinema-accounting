# Generated by Django 4.2.7 on 2024-09-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0012_remove_ticket_is_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='end_time',
            field=models.TimeField(verbose_name='end time'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='start_time',
            field=models.TimeField(verbose_name='start time'),
        ),
    ]
