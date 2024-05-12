# Generated by Django 5.0.4 on 2024-05-12 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('difficulty_level', '0001_initial'),
        ('rutine_type', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('difficulty_level_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='difficulty_level.difficultylevel')),
                ('rutine_type_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rutine_type.rutinetype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.user')),
            ],
        ),
    ]
