# Generated by Django 4.0.6 on 2022-07-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='day',
            field=models.IntegerField(),
        ),
    ]
