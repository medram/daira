# Generated by Django 3.0.2 on 2020-07-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200713_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, default='ABCD', max_length=150, null=True),
        ),
    ]