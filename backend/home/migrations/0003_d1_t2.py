# Generated by Django 2.2.28 on 2023-12-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_d1"),
    ]

    operations = [
        migrations.AddField(
            model_name="d1",
            name="t2",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]