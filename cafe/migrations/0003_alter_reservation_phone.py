# Generated by Django 4.1.7 on 2023-02-19 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0002_remove_reservation_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="phone",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]