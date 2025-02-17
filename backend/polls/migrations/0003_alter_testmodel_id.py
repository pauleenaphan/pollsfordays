# Generated by Django 4.1.13 on 2024-10-16 19:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_alter_testmodel_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testmodel",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
