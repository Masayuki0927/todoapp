# Generated by Django 4.0 on 2021-12-12 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todomodel_duedate_todomodel_mail_todomodel_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='mail',
        ),
    ]
