# Generated by Django 3.0.6 on 2020-05-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_auto_20200517_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomrate',
            name='lang',
            field=models.CharField(choices=[('fa', 'Farsi'), ('eng', 'English')], default='fa', max_length=20),
        ),
    ]
