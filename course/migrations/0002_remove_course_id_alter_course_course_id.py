# Generated by Django 5.0.6 on 2024-07-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]