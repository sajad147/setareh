# Generated by Django 3.0.6 on 2020-05-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_newsslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clocklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('address', models.TextField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='newsslider',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]