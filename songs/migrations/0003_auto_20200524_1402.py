# Generated by Django 3.0.5 on 2020-05-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_poetry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(),
        ),
    ]
