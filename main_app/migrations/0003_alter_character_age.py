# Generated by Django 4.1.3 on 2022-11-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_prounoun_character_pronoun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='age',
            field=models.CharField(max_length=20),
        ),
    ]
