# Generated by Django 4.0.4 on 2022-12-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0029_infomf'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDiscord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.CharField(blank=True, max_length=255, null=True)),
                ('discord_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
