# Generated by Django 4.2.7 on 2024-09-14 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0010_remove_revenue_cinema'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='cinema',
        ),
    ]
