# Generated by Django 4.0.4 on 2022-11-22 14:02

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_rename_desc_about_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coreteam',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]