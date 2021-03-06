# Generated by Django 3.1.2 on 2020-11-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_class', '0002_workoutclass_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutclass',
            name='equipment',
        ),
        migrations.AddField(
            model_name='workoutclass',
            name='equipment',
            field=models.ManyToManyField(blank=True, null=True, to='workout_class.Equipment'),
        ),
        migrations.AlterField(
            model_name='workoutclass',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
