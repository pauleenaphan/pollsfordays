# Generated by Django 4.1.13 on 2024-10-17 14:04

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0012_alter_pollmodel_author_alter_pollmodel_choices_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pollmodel",
            name="choices",
            field=djongo.models.fields.JSONField(max_length=100),
        ),
    ]
