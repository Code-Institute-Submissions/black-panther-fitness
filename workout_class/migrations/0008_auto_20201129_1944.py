# Generated by Django 3.1.2 on 2020-11-29 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_class', '0007_auto_20201129_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutclass',
            name='day',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
    ]
