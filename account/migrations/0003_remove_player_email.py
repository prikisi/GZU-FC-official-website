# Generated by Django 4.2.7 on 2023-11-21 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='email',
        ),
    ]
