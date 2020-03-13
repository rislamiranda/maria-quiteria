# Generated by Django 3.0 on 2020-03-13 18:16

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gazette",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("crawled_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("crawled_from", models.URLField()),
                ("notes", models.TextField(blank=True, null=True)),
                ("date", models.DateField()),
                (
                    "power",
                    models.CharField(
                        choices=[
                            ("executivo", "Poder Executivo"),
                            ("legislativo", "Poder Legislativo"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "year_and_edition",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "file_urls",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.URLField(blank=True, null=True),
                        blank=True,
                        size=None,
                    ),
                ),
                ("file_content", models.TextField(blank=True, null=True)),
            ],
            options={"abstract": False,},
        ),
        migrations.AlterField(
            model_name="citycouncilagenda",
            name="crawled_from",
            field=models.URLField(
                default="https://www.transparencia.feiradesantana.ba.leg.br/index.php?view=inicio"
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="GazetteEvent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("crawled_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("crawled_from", models.URLField()),
                ("notes", models.TextField(blank=True, null=True)),
                ("title", models.CharField(blank=True, max_length=300, null=True)),
                (
                    "secretariat",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("summary", models.TextField(blank=True, null=True)),
                (
                    "gazette",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datasets.Gazette",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]