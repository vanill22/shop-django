# Generated by Django 3.0.8 on 2021-02-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210211_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена'),
        ),
    ]
