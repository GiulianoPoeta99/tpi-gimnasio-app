# Generated by Django 5.0.4 on 2024-05-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Nivel de dificultad',
                'verbose_name_plural': 'Niveles de dificultad',
                'ordering': ['name'],
            },
        ),
    ]
