# Generated by Django 2.1.7 on 2019-03-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comarca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobbit',
            name='feet_size',
            field=models.FloatField(default=20.0),
        ),
    ]
