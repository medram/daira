# Generated by Django 3.1 on 2020-09-15 22:52

import daira.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sokna', '0006_auto_20200712_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soknarequest',
            name='terms_of_use',
            field=models.BooleanField(default=True, validators=[daira.validators.TermsOfUse], verbose_name='I confess that all the above information are correct.'),
        ),
    ]
