# Generated by Django 5.1.6 on 2025-03-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_jobs_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
