# Generated by Django 3.0.7 on 2020-09-08 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200905_0123'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_teacher_username',
            field=models.OneToOneField(blank=True, choices=[], null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
        ),
    ]
