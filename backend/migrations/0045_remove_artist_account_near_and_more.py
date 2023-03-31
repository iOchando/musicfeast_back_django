# Generated by Django 4.0.4 on 2023-03-31 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0044_rename_suscribe_subscribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='account_near',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='account_near_tax',
        ),
        migrations.AddField(
            model_name='artist',
            name='order_list',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
