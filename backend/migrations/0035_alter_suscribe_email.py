# Generated by Django 4.0.4 on 2023-01-20 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0034_suscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscribe',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
