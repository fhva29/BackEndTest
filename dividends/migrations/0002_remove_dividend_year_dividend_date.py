# Generated by Django 4.2.5 on 2023-09-07 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dividends", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dividend",
            name="year",
        ),
        migrations.AddField(
            model_name="dividend",
            name="date",
            field=models.CharField(default=2023, max_length=255),
            preserve_default=False,
        ),
    ]
