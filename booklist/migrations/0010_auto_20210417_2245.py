# Generated by Django 3.1.7 on 2021-04-17 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0009_auto_20210417_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='writer',
            old_name='tage',
            new_name='wage',
        ),
        migrations.RenameField(
            model_name='writer',
            old_name='tname',
            new_name='wname',
        ),
    ]
