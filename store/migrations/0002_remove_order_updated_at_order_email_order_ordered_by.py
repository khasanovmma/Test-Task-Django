# Generated by Django 4.1.1 on 2022-09-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="order",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="ordered_by",
            field=models.CharField(max_length=120, null=True),
        ),
    ]
