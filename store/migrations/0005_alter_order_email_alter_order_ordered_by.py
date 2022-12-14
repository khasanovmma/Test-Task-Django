# Generated by Django 4.1.1 on 2022-09-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_by',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
