# Generated by Django 4.2.4 on 2023-08-01 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
