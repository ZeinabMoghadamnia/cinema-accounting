# Generated by Django 4.2.7 on 2024-09-08 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor'),
        ),
    ]
