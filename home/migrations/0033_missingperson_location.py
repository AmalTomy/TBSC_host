# Generated by Django 4.2.17 on 2025-01-12 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_missingperson_aadhar_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingperson',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
