# Generated by Django 4.1.3 on 2022-11-09 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='prounoun',
            new_name='pronoun',
        ),
    ]
