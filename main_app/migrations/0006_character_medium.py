# Generated by Django 4.1.3 on 2022-11-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_medium_alter_title_options_alter_title_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='medium',
            field=models.ManyToManyField(to='main_app.medium'),
        ),
    ]
