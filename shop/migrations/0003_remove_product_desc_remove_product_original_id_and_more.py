# Generated by Django 5.0.3 on 2024-03-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_sitedetail"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="desc",
        ),
        migrations.RemoveField(
            model_name="product",
            name="original_id",
        ),
        migrations.AlterField(
            model_name="sitedetail",
            name="address",
            field=models.CharField(default="234, Lagos, Nigeria", max_length=500),
        ),
    ]
