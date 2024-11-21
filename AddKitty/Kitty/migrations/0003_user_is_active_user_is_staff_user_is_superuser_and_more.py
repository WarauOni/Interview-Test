# Generated by Django 4.0 on 2024-11-19 18:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Kitty', '0002_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
