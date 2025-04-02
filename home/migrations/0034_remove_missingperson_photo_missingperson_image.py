# Generated by Django 5.0.6 on 2025-01-12 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_missingperson_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missingperson',
            name='photo',
        ),
        migrations.AddField(
            model_name='missingperson',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='missing_persons/'),
        ),
    ]
