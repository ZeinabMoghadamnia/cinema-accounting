# Generated by Django 4.2.7 on 2024-09-14 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial_report', '0001_initial'),
        ('vendor', '0003_alter_purchase_cost_alter_purchase_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='cost',
            field=models.IntegerField(verbose_name='cost'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='item_name',
            field=models.CharField(max_length=50, verbose_name='item name'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.IntegerField(verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='tax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='financial_report.tax', verbose_name='tax'),
        ),
    ]
