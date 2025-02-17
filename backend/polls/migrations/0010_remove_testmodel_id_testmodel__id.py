# Generated by Django 4.1.13 on 2024-10-17 00:55

import bson.objectid
from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0009_remove_testmodel__id_testmodel_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="testmodel",
            name="id",
        ),
        migrations.AddField(
            model_name="testmodel",
            name="_id",
            field=djongo.models.fields.ObjectIdField(
                auto_created=True,
                default=bson.objectid.ObjectId,
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
