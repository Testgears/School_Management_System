# Generated by Django 3.0.7 on 2020-09-10 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_remove_teacher_designation'),
        ('classes', '0008_auto_20200910_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_teacher',
            field=models.OneToOneField(blank=True, choices=[('abc', 'abc')], null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(blank=True, choices=[('abc', 'abc')], null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
        ),
    ]
