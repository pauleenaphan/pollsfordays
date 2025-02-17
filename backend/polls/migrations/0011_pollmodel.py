# Generated by Django 4.1.13 on 2024-10-17 03:47

import bson.objectid
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0010_remove_testmodel_id_testmodel__id"),
    ]

    operations = [
        migrations.CreateModel(
            name="PollModel",
            fields=[
                (
                    "_id",
                    djongo.models.fields.ObjectIdField(
                        auto_created=True,
                        default=bson.objectid.ObjectId,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("choices", djongo.models.fields.JSONField(max_length=100)),
                ("author", models.CharField(max_length=20)),
                ("timeLimit", models.IntegerField()),
                ("datePosted", models.IntegerField()),
            ],
        ),
    ]
