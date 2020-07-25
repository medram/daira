# Generated by Django 3.0.2 on 2020-07-25 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daira', '0008_auto_20200712_1826'),
        ('account', '0005_auto_20200721_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='moh7aka',
        ),
        migrations.AddField(
            model_name='customuser',
            name='mol7aka',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='daira.Mol7aka', verbose_name='Administrative attache'),
        ),
    ]
