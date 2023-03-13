# Generated by Django 4.0.4 on 2022-12-20 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_alter_userdiscord_wallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistDiscord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.CharField(blank=True, max_length=255, null=True)),
                ('artist', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.artist')),
            ],
        ),
    ]
