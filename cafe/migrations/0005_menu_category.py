# Generated by Django 4.1.7 on 2023-03-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0004_menu"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="category",
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
    ]
