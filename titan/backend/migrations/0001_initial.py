# Generated by Django 4.1.7 on 2023-03-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Price",
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
                ("ticker", models.CharField(max_length=10)),
                ("commodity", models.CharField(max_length=100)),
                ("date", models.DateTimeField()),
                ("open", models.FloatField()),
                ("high", models.FloatField()),
                ("low", models.FloatField()),
                ("close", models.FloatField()),
                ("volume", models.IntegerField()),
            ],
            options={
                "unique_together": {("ticker", "date")},
            },
        ),
    ]
