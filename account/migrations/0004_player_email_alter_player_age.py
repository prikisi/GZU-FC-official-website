# Generated by Django 4.2.7 on 2023-11-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_player_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
