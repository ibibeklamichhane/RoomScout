# Generated by Django 2.2.4 on 2019-08-29 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0007_auto_20190828_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billset',
            name='date',
        ),
        migrations.AddField(
            model_name='billset',
            name='month',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='billset',
            name='year',
            field=models.IntegerField(default=-1),
        ),
    ]