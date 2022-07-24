# Generated by Django 4.0.6 on 2022-07-23 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('month', models.IntegerField(default=3)),
                ('day', models.IntegerField(max_length=3)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
