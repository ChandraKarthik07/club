# Generated by Django 4.1.1 on 2023-06-12 08:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
