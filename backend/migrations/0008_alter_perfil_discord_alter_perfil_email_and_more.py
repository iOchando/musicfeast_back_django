# Generated by Django 4.0.4 on 2022-10-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_perfil_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='discord',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='instagram',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telegram',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='twitter',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]