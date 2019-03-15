# Generated by Django 2.1.7 on 2019-03-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('breakfast', models.IntegerField(default=5)),
                ('evil', models.BooleanField(default=False)),
                ('ring', models.BooleanField(default=False)),
                ('hungry', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Hobbit',
            },
        ),
    ]
