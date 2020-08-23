# Generated by Django 3.0.2 on 2020-08-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daira', '0009_auto_20200816_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='social_status',
            field=models.IntegerField(choices=[(0, 'Unknown'), (1, 'Single'), (2, 'Married'), (3, 'Divorced')], default=0),
        ),
        migrations.AlterField(
            model_name='individual',
            name='ar_firstname',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Firstname in Arabic'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='ar_lastname',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Lastname in Arabic'),
        ),
    ]