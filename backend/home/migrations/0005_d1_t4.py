# Generated by Django 2.2.28 on 2023-12-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_d1_t3"),
    ]

    operations = [
        migrations.AddField(
            model_name="d1",
            name="t4",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
