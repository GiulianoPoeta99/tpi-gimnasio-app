# Generated by Django 5.0.4 on 2024-07-02 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muscle_exercise', '0002_alter_muscleexercise_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='muscleexercise',
            options={'ordering': ['name'], 'verbose_name': 'Músculo', 'verbose_name_plural': 'Músculos'},
        ),
    ]
