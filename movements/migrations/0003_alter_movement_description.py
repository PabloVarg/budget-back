# Generated by Django 4.2.5 on 2023-09-24 00:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movements", "0002_alter_movement_options_movement_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movement",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
