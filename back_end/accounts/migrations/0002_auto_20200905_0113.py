# Generated by Django 3.0.7 on 2020-09-05 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'Administrator'), (1, 'Teacher'), (2, 'Class teacher'), (3, 'Headmaster'), (4, 'Student')], null=True),
        ),
    ]
