# Generated by Django 5.1.6 on 2025-04-03 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_jobs_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='website',
            field=models.CharField(default='glassdoor', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.CharField(default='', max_length=50),
        ),
    ]
