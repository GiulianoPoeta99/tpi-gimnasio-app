# Generated by Django 5.0.4 on 2024-05-29 16:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercise', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='exercises', to=settings.AUTH_USER_MODEL),
        ),
    ]
