# Generated by Django 3.0.8 on 2020-10-19 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NetworkEdge",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="NetworkNode",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                (
                    "children",
                    models.ManyToManyField(
                        blank=True, related_name="parents", through="tests.NetworkEdge", to="tests.NetworkNode"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="networkedge",
            name="child",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="NetworkNode_parent", to="tests.NetworkNode"
            ),
        ),
        migrations.AddField(
            model_name="networkedge",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="NetworkNode_child", to="tests.NetworkNode"
            ),
        ),
    ]
