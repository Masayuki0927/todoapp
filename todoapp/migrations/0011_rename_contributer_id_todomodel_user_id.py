# Generated by Django 4.0 on 2021-12-14 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0010_rename_contributer_todomodel_contributer_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='contributer_ID',
            new_name='user_id',
        ),
    ]