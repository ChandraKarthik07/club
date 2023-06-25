# Generated by Django 4.1.1 on 2023-06-19 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0009_user_otp"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookings",
            name="product_list",
        ),
        migrations.CreateModel(
            name="BookingProduct",
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
                ("quantity", models.IntegerField(default=1)),
                (
                    "booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="club.bookings"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="club.products"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bookings",
            name="product_list",
            field=models.ManyToManyField(
                through="club.BookingProduct", to="club.products"
            ),
        ),
    ]