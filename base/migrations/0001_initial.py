# Generated by Django 5.2 on 2025-04-22 14:40

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
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
                (
                    "total_amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("is_paid", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "carts",
            },
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("message", models.TextField()),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "feedback",
            },
        ),
        migrations.CreateModel(
            name="Sneaker",
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
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("category", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "surface_type",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("composition", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("unisex", "Unisex"),
                        ],
                        max_length=7,
                    ),
                ),
                ("sizes", models.JSONField(blank=True, default=dict)),
            ],
            options={
                "db_table": "sneakers",
            },
        ),
        migrations.CreateModel(
            name="User",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("male", "Male"), ("female", "Female")],
                        max_length=6,
                        null=True,
                    ),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "passport_series",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "passport_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
            ],
            options={
                "db_table": "users",
            },
        ),
        migrations.CreateModel(
            name="CartItem",
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
                (
                    "size",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.cart"
                    ),
                ),
                (
                    "sneaker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.sneaker"
                    ),
                ),
            ],
            options={
                "db_table": "cart_items",
            },
        ),
        migrations.AddField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="base.user"
            ),
        ),
        migrations.CreateModel(
            name="BankCard",
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
                ("card_number", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.user"
                    ),
                ),
            ],
            options={
                "db_table": "bank_cards",
            },
        ),
    ]
