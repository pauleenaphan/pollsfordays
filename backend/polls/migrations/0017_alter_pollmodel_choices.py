# Generated by Django 4.1.13 on 2024-10-21 20:50

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0016_alter_pollmodel_choices"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pollmodel",
            name="choices",
            field=djongo.models.fields.JSONField(),
        ),
    ]
