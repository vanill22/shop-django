# Generated by Django 3.0.8 on 2021-02-11 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210211_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Customer', verbose_name='Владелец'),
        ),
    ]
