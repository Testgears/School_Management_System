# Generated by Django 3.0.7 on 2020-08-29 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='previous_school',
            field=models.CharField(max_length=200),
        ),
    ]
