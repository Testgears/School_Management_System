# Generated by Django 3.0.7 on 2020-09-20 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0025_auto_20200920_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Subject'),
        ),
    ]