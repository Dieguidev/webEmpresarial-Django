# Generated by Django 5.0 on 2023-12-16 03:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Fecha de publicacion"
            ),
        ),
    ]
