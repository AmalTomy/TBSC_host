# Generated by Django 5.0.6 on 2024-10-01 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_busreschedule_schedule_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentjob',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
