# Generated by Django 2.0 on 2018-06-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controler',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
