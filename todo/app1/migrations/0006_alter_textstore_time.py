# Generated by Django 5.1.7 on 2025-03-31 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_textstore_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textstore',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
