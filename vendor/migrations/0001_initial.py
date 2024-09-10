# Generated by Django 4.2.7 on 2024-09-10 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='date updated')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='delete status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='date deleted')),
                ('restored_at', models.DateTimeField(blank=True, null=True, verbose_name='date restored')),
                ('address', models.CharField(max_length=120, verbose_name='address')),
                ('company_name', models.CharField(max_length=50, verbose_name='company name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='date updated')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='delete status')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='date deleted')),
                ('restored_at', models.DateTimeField(blank=True, null=True, verbose_name='date restored')),
                ('amount', models.IntegerField(verbose_name='amount')),
                ('description', models.CharField(max_length=120, verbose_name='description')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='vendor.vendor', verbose_name='vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
