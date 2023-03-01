# Generated by Django 4.1.7 on 2023-03-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0006_alter_menu_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location", models.CharField(max_length=555)),
                ("phone_number", models.CharField(max_length=55)),
                ("email", models.CharField(blank=True, max_length=55, null=True)),
                ("body", models.TextField(blank=True, null=True)),
            ],
        ),
    ]