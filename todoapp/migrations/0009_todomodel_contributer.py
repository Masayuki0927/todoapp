# Generated by Django 4.0 on 2021-12-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_alter_todomodel_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='contributer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
