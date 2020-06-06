# Generated by Django 3.0.2 on 2020-06-05 21:54

import daira.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sokna', '0002_auto_20200605_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soknarequest',
            name='born_d',
            field=models.IntegerField(blank=True, null=True, verbose_name='Day of birthday'),
        ),
        migrations.AlterField(
            model_name='soknarequest',
            name='born_m',
            field=models.IntegerField(blank=True, null=True, verbose_name='Month of birthday'),
        ),
        migrations.AlterField(
            model_name='soknarequest',
            name='born_y',
            field=models.IntegerField(blank=True, null=True, verbose_name='Year of birthday'),
        ),
        migrations.AlterField(
            model_name='soknarequest',
            name='phone',
            field=models.BigIntegerField(validators=[daira.validators.PhoneValidator]),
        ),
    ]
