# Generated by Django 5.0.4 on 2024-05-12 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('difficulty_level', '__first__'),
        ('exercise_type', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dificulty_level_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='difficulty_level.difficultylevel')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.user')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='exercise_type.exercisetype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='exercises', to='user.user')),
            ],
        ),
    ]
