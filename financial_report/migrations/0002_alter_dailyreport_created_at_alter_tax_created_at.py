# Generated by Django 4.2.7 on 2024-09-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date created'),
        ),
    ]
