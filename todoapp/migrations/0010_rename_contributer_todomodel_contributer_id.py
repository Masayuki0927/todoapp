# Generated by Django 4.0 on 2021-12-14 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0009_todomodel_contributer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='contributer',
            new_name='contributer_ID',
        ),
    ]
