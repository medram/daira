# Generated by Django 3.0.2 on 2020-06-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sokna', '0004_auto_20200606_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='soknarequest',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
