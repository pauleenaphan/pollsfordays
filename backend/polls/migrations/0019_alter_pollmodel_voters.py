# Generated by Django 4.1.13 on 2024-10-22 02:42

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0018_pollmodel_voters"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pollmodel",
            name="voters",
            field=djongo.models.fields.JSONField(default=list),
        ),
    ]
