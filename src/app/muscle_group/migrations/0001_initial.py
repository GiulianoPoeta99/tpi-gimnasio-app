# Generated by Django 5.0.4 on 2024-05-12 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercise', '0001_initial'),
        ('muscle_exercise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='exercise.exercise')),
                ('muscle_exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='muscle_exercise.muscleexercise')),
            ],
        ),
    ]
