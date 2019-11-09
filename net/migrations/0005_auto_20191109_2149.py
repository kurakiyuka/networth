# Generated by Django 2.2.6 on 2019-11-09 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net', '0004_auto_20191109_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='market_prefix',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='total_price_in_RMB',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]