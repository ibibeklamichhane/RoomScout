# Generated by Django 2.2.4 on 2019-08-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('houses', '0003_auto_20190815_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='bike_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='transit_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='walk_score',
            field=models.IntegerField(default=0),
        ),
    ]
