# Generated by Django 3.0.5 on 2020-06-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_mysongs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysongs',
            name='DateCompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
