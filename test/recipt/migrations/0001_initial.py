# Generated by Django 4.2.2 on 2023-06-29 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=24, verbose_name="카테고리명")),
            ],
        ),
        migrations.CreateModel(
            name="Recipt",
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
                ("devceId", models.CharField(max_length=125, verbose_name="디바이스ID")),
                ("date", models.DateField(verbose_name="결제일")),
                ("store", models.CharField(max_length=125, verbose_name="영업점")),
                ("address", models.CharField(max_length=125, verbose_name="주소")),
                ("list", models.CharField(max_length=125, verbose_name="상품목록")),
                ("amount", models.IntegerField(verbose_name="결제금액")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipt.category",
                        verbose_name="카테고리",
                    ),
                ),
            ],
        ),
    ]
