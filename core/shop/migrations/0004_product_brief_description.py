# Generated by Django 4.2.11 on 2024-04-10 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_rename_descrption_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="brief_description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
